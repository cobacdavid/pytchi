__author__ = "david cobac"
__email__ = "david.cobac @ gmail.com"
__twitter__ = "https://twitter.com/david_cobac"
__github__ = "https://github.com/cobacdavid"
__copyright__ = "Copyright 2021, CC-BY-NC-SA"

from urllib.parse import urlparse, parse_qs
from .lib import ytdown
from .lib import imgcc


class pytci:
    def __init__(self, url):
        # https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        urldata = urlparse(url)
        self._vid = parse_qs(urldata.query)['v'][0]
        self.video_obj = ytdown.ytdown(self._vid)
        self.video_obj.down()
        self._step = 1
        self.video_obj.pas = self._step

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, pas_en_s):
        self._step = pas_en_s
        self.video_obj.pas = self._step

    def to_img(self, taille=None):
        self.video_obj.vers_photos()
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir,
                                  taille)
        self.cc_obj.traitement()
        self.cc_obj.save(self._vid)

    def to_svg(self, taille=None):
        self.video_obj.vers_photos()
        self.cc_obj = imgcc.imgcc(self.video_obj._img_fulldir,
                                  taille,
                                  filefmt='svg')
        self.cc_obj.traitement()
        self.cc_obj.save(self._vid)
