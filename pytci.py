__author__ = "david cobac"
__email__ = "david.cobac @ gmail.com"
__twitter__ = "https://twitter.com/david_cobac"
__github__ = "https://github.com/cobacdavid"
__copyright__ = "Copyright 2021, CC-BY-NC-SA"


from urllib.parse import urlparse, parse_qs
from .yt_down import *
from .imgcc import *


class pytci:
    def __init__(self, url):
        # https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        urldata = urlparse(url)
        vid = parse_qs(urldata.query)['v'][0]
        self.video_obj = ytdown(vid)
        self.video_obj.down()
        self.video_obj.vers_photos()

    def to_img(self):
        self.cc_obj = imgcc(self.video_obj._img_fulldir)
        self.cc_obj.traitement()
        self.cc_obj.save()

    def to_plt(self):
        self.cc_obj = imgcc(self.video_obj._img_fulldir)
        self.cc_obj.traitement()
        self.cc_obj.show()
