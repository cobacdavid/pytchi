from urllib.parse import urlparse, parse_qs
from .lib import ytdown
from .lib import imgcc
import pytube
import slugify


class pytchi:

    """This class uses YT URLs to produce images from YT videos.
    Images are made of concentric circles. Each circle is made
    joining little arcs whose color is taken from an image of the
    video. Outermost circles are the first images and innermost are
    last images.

    Two outputs are currently available : 'png' and 'svg'

    :param str url: URL of YT video to convert in pytchi image

    .. note:: In case URL contains a (play)list variable, all
              videos from the playlist will be treated.

    .. note:: This class is just a wrapper of the pytchiv class
              which is intended to treat a single video.

    :Example:

    >>> o = pytchi.pytchi('https://www.youtube.com/watch?v=IjxkCokODEs')
    >>> o.to_img() # export to png (auto dimension)
    >>> o.to_img(1080) # or with desired image's dimension
    >>> p = pytchi.pytchi('https://www.youtube.com/watch?v=PVyS9JwtFoQ')
    >>> p.step = 2 # every 2 seconds of the video (default is 1)
    >>> p.xmth = 'random'
    >>> p.to_svg() # export to svg>>> import pytchi
    >>> q = pytchi.pytchi('https://www.youtube.com/watch?v=gxAaO2rsdIs&list=PLZHQObOWTQDOcxqQ36Vow3TdTRjkdSvT-') # a playlist of 3 videos
    >>> q.to_img() # 3 images will be output

    """

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
        self._reverse = False

        self._obj_list = []
        for video in self._list:
            self._obj_list.append(pytchiv(video))

    @property
    def step(self):
        """Step in s between images extracted from YT videos
        default is 1s
        """

        return self._step

    @step.setter
    def step(self, pas_en_s):
        """ Step in s between images extracted from YT videos

        :param pas_en_s: Step in s
        :type pas_en_s: float or int
        """

        self._step = pas_en_s
        for obj in self._obj_list:
            obj.step = self._step

    @property
    def xmth(self):
        """Getter of xmth property
        """

        return self._xmth

    @xmth.setter
    def xmth(self, exmeth):
        """Extraction method of colors : 'random' (line) or 'diagonal'
        default is 'diagonal'
        """

        self._xmth = exmeth
        for obj in self._obj_list:
            obj.xmth = self._xmth

    @property
    def reverse(self):
        """Getter of reverse property.
        """

        return self._reverse

    @reverse.setter
    def reverse(self, reverse_choice):
        """Set to True, it reverses images order (default to False).
        """

        self._reverse = reverse_choice
        for obj in self._obj_list:
            obj.reverse = reverse_choice

    def to_img(self, taille=None):
        """Outputs PNG image files

        :param taille: Dimension in pixels of output image
        :type taille: int

        .. note:: This function creates PNG files whose name is YT
                  video title prefixed with pytchi and YT unique id
        """

        for obj in self._obj_list:
            obj.to_img(taille)

    def to_svg(self, taille=None):
        """Outputs SVG image file using YT video unique id.

        :param taille: Dimension in points of output image
                       1 point = 1/72 inch
        :type taille: float

        .. note:: This function creates SVG files whose name is YT
                  video title prefixed with pytchi and YT unique id
        """

        for obj in self._obj_list:
            obj.to_svg(taille)

    def clean(self):
        """Deletes downloaded videos and video images directories.
        Does not delete pytchi images.
        """

        for obj in self._obj_list:
            obj.clean()


class pytchiv:

    """This class uses YT URLs to produce an image from one YT
    video. This image is made of concentric circles. Each circle is
    made joining little arcs whose color is taken from an image of
    the video. Outermost circles are the first images and innermost
    are last images.

    Two outputs are currently available : 'png' and 'svg'

    :param str url: URL of YT video to convert in pytchi image

    .. note:: pytchi chooses the worst quality of video offered by
              YT for best download time

    :Example:

    >>> o = pytchi.pytchiv('https://www.youtube.com/watch?v=IjxkCokODEs')
    >>> o.to_img() # export to png
    >>> o.to_img(1080) # or with desired image's dimension
    >>> p = pytchi.pytchiv('https://www.youtube.com/watch?v=PVyS9JwtFoQ')
    >>> p.step = 2 # every 2 seconds of the video (default is 1)
    >>> p.to_svg() # export to svg>>> import pytchi

    """

    def __init__(self, url):
        """Constructor"""

        # https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        urldata = urlparse(url)
        self._vid = parse_qs(urldata.query)['v'][0]
        self.video_obj = ytdown.ytdown(self._vid)
        self.video_obj.down()
        self._name = slugify.slugify(
            f"pytchi-{self._vid}-{self.video_obj._yt.title}"
        )
        self._step = 1
        self._xmth = 'diagonal'
        self._reverse = False
        self.video_obj.pas = self._step

    @property
    def step(self):
        """Getter of step property
        """

        return self._step

    @step.setter
    def step(self, pas_en_s):
        """ Step in s between images extracted from the YT video
        Default set to 1s

        :param pas_en_s: Step in s
        :type pas_en_s: float or int
        """

        self._step = pas_en_s
        self.video_obj.step = self._step

    @property
    def xmth(self):
        """Getter of xmth property
        """

        return self._xmth

    @xmth.setter
    def xmth(self, exmeth):
        """Extraction method of colors : 'random' (line) or 'diagonal'
        default is 'diagonal'
        """

        self._xmth = exmeth

    @property
    def reverse(self):
        """Getter of reverse property.
        """

        return self._reverse

    @reverse.setter
    def reverse(self, reverse_choice):
        """Set to True, it reverses images order (default to False).
        """

        self._reverse = reverse_choice

    def to_img(self, taille=None):
        """Outputs PNG image file using YT video unique id.

        :param taille: Dimension in pixels of output image
        :type taille: int

        .. note:: This function creates a PNG file whose name is YT
                  video unique id.
        """

        self.video_obj.to_images()
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir, taille,
                                  xmth=self._xmth,
                                  reverse=self._reverse)
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
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir, taille,
                                  filefmt='svg',
                                  xmth=self._xmth,
                                  reverse=self._reverse
                                  )
        self.cc_obj.apply()
        self.cc_obj.save(self._name)

    def clean(self, all=False):
        """Deletes video images directory and possibly downloaded video
        Does not delete pytchi image.
        """

        self.video_obj.clean(all)
