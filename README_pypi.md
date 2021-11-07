# PYTCHI

**P**ython **Y**ou**T**ube **C**oncentric **C**ircles **I**mage

> _You_ Huh?? No **H** in pytcci?
>
> _Me_ Are you serious?


## Installation

`pip3 install pytchi`

_Dependancies:_

- `opencv-python-headless`
- `pycairo`
- `python-slugify`
- `pytube`


## Usage

Following code produces:

- two PNG images: first with concentric circles, second with lines
from [this video](https://www.youtube.com/watch?v=EelPrEojesM);
- one PNG image (1000px width) with concentric circles from [this
video](https://www.youtube.com/watch?v=IjxkCokODEs)
- one SVG file with concentric circles from [this
video](https://www.youtube.com/watch?v=PVyS9JwtFoQ) using 1 image
every 2 seconds and then cleans for it only remains the final image
- 3 PNG images with concentric circles from [this
  playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOcxqQ36Vow3TdTRjkdSvT-)
  using `diagonal` line extraction instead of `random` (default)
  and reversing images: innermost for first images. Note that URL
  has just to contain a `list` variable so that `pytchi` produces
  an image for each video of that playlist.  Each image is 800x800
  pixels.

```python3

import pytchi
import os


# 
o = pytchi.pytchi('https://www.youtube.com/watch?v=EelPrEojesM')
o.to_img() # export to png (concentric circles)
o.shape = 'lines'
o.to_img() # export to png (rectangle with lines)
#
p = pytchi.pytchi('https://www.youtube.com/watch?v=IjxkCokODEs')
p.to_img(1_000) # outputs a 1000px image
#
q = pytchi.pytchi('https://www.youtube.com/watch?v=PVyS9JwtFoQ')
q.step = 2 # every 2 seconds of the video (default is 1)
q.to_svg() # export to svg
q.clean(all) # deletes temporary files so that p object is unsable now!
#
# playlist: treat several videos
r = pytchi.pytchi('https://www.youtube.com/watch?v=gxAaO2rsdIs&list=PLZHQObOWTQDOcxqQ36Vow3TdTRjkdSvT-')
r.xmth = 'diagonal' # change extraction method
r.reverse = True # reverse order of inserted images
r.to_img(800)

```

## Outputs

- [EelPrEojesM](https://www.youtube.com/watch?v=EelPrEojesM)

<img width="37.5%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-eelpreojesm-the-eden-house-sin.png"></img>
<img width="37.5%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-eelpreojesm-the-eden-house-sin__lines.png"></img>

- [IjxkCokODEs](https://www.youtube.com/watch?v=IjxkCokODEs)

<img width="75%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-ijxkcokodes-talk-to-her-zodiac-official-video.png"></img>

- [PVyS9JwtFoQ](https://www.youtube.com/watch?v=PVyS9JwtFoQ)

<img width="75%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-pvys9jwtfoq-pixies-debaser-official-video.svg"></img>

- [D__UaR5MQao](pytchi-d-uar5mqao-the-dp-3t-algorithm-for-contact-tracing-via-nicky-case.png) / [gxAaO2rsdIs](pytchi-gxaao2rsdis-simulating-an-epidemic.png) / [Kas0tIxDvrg](pytchi-kas0tixdvrg-exponential-growth-and-epidemics.png)

<img width="25%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-d-uar5mqao-the-dp-3t-algorithm-for-contact-tracing-via-nicky-case.png"></img>
<img width="25%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-gxaao2rsdis-simulating-an-epidemic.png"></img>
<img width="25%" src="https://github.com/cobacdavid/pytchi/blob/main/examples/pytchi-kas0tixdvrg-exponential-growth-and-epidemics.png"></img>

## Copyright

2021 / D. COBAC / CC-BY-NC-SA
