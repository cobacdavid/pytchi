from urllib.parse import urlparse, parse_qs
from .lib import ytdown
from .lib import imgcc
import pytube
import slugify


class pytci:
    def __init__(self, url):
        """Constructor"""

        urldata = urlparse(url)
        dico_query_urldata = parse_qs(urldata.query)
        self._list = None
        if 'list' in dico_query_urldata:
            self._list = pytube.contrib.playlist.Playlist(url)
        elif 'v' in dico_query_urldata:
            self._list = [url]
        else:
            pass

        self._step = 1
        self._xmth = 'diagonal'

        self._obj_list = []
        for video in self._list:
            self._obj_list.append(pytciv(video))

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, pas_en_s):
        self._step = pas_en_s
        for obj in self._obj_list:
            obj.step = self._step

    @property
    def xmth(self):
        return self._xmth

    @xmth.setter
    def xmth(self, exmeth):
        self._xmth = exmeth
        for obj in self._obj_list:
            obj.xmth = self._xmth

    def to_img(self, taille=None):
        for obj in self._obj_list:
            obj.to_img(taille)

    def to_svg(self, taille=None):
        for obj in self._obj_list:
            obj.to_svg(taille)


class pytciv:

    """This class uses YT URLs to produce an image. This image is made
    of concentric circles. Each circle is made joining little arcs
    whose color is taken from an image of the video. Outermost
    circles are the first images and innermost are last images.

    Two outputs are currently available : 'png' and 'svg'

    :param str url: URL of YT video to convert in pytci image

    .. note:: pytci chooses the worst quality of video offered by
              YT for best download time

    :Example:

    >>> o = pytci.pytci('https://www.youtube.com/watch?v=IjxkCokODEs')
    >>> o.to_img() # export to png
    >>> o.to_img(1080) # or with desired image's dimension
    >>> p = pytci.pytci('https://www.youtube.com/watch?v=PVyS9JwtFoQ')
    >>> p.step = 2 # every 2 seconds of the video (default is 1)
    >>> p.to_svg() # export to svg>>> import pytci
    >>> o = pytci.pytci

    """

    def __init__(self, url):
        """Constructor"""

        # https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        urldata = urlparse(url)
        self._vid = parse_qs(urldata.query)['v'][0]
        self.video_obj = ytdown.ytdown(self._vid)
        self.video_obj.down()
        self._name = slugify.slugify(
            f"pytci-{self._vid}-{self.video_obj._yt.title}"
        )
        self._step = 1
        self._xmth = 'diagonal'
        self.video_obj.pas = self._step

    @property
    def step(self):
        """Step in s between images extracted from the YT video
        default is 1s
        """

        return self._step

    @step.setter
    def step(self, pas_en_s):
        """ Step in s between images extracted from the YT video

        :param pas_en_s: Step in s
        :type pas_en_s: float or int
        """

        self._step = pas_en_s
        self.video_obj.step = self._step

    @property
    def xmth(self):
        """Extraction method of colors : 'random' (line) or 'diagonal'
        default is 'diagonal'
        """

        return self._xmth

    @xmth.setter
    def xmth(self, exmeth):
        """Extraction method of colors : 'random' (line) or 'diagonal'
        default is 'diagonal'
        """

        self._xmth = exmeth

    def to_img(self, taille=None):
        """Outputs PNG image file using YT video unique id.

        :param taille: Dimension in pixels of output image
        :type taille: int

        .. note:: This function creates a PNG file whose name is YT
                  video unique id.
        """

        self.video_obj.to_images()
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir,
                                  taille, xmth=self._xmth)
        self.cc_obj.apply()
        self.cc_obj.save(self._name)

    def to_svg(self, taille=None):
        """Outputs SVG image file using YT video unique id.

        :param taille: Dimension in points of output image
                       1 point = 1/72 inch
        :type taille: float

        .. note:: This function creates a SVG file whose name is YT
                  video unique id.
        """

        self.video_obj.to_images()
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir,
                                  taille,
                                  filefmt='svg')
        self.cc_obj.apply()
        self.cc_obj.save(self._name)
