# pytci

**P**ython **Y**ou**T**ube concentric **C**ircles **I**mage

## Installation

`pip3 install pytci`

_Dependances:_

- `opencv-python-headless`
- `pycairo`
- `python-slugify`


## Usage

Following console code produces:

- a PNG image from [this
  video](https://www.youtube.com/watch?v=IjxkCokODEs) then replaces
  it with a fixed width 1080px image ;
- a SVG image from [this
  video](https://www.youtube.com/watch?v=PVyS9JwtFoQ) using 1 image
  every 2 seconds and then cleans for it only remains the final image
- 3 PNG images from [this
  playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOcxqQ36Vow3TdTRjkdSvT-)
  using `random` line extraction instead of `diagonal`
  (default). Note that URL has just to contain a `list` variable so
  that `pytci` produces an image for each video of that playlist.

```python3

>>> import pytci
>>> o = pytci.pytci('https://www.youtube.com/watch?v=IjxkCokODEs')
>>> o.to_img() # export to png
>>> o.to_img(1080) # or with desired image's dimension
>>> p = pytci.pytci('https://www.youtube.com/watch?v=PVyS9JwtFoQ')
>>> p.step = 2 # every 2 seconds of the video (default is 1)
>>> p.to_svg() # export to svg
>>> p.clean(all) # deletes temporary files so that p object is unsable now!
>>> q = pytci.pytci('https://www.youtube.com/watch?v=gxAaO2rsdIs&list=PLZHQObOWTQDOcxqQ36Vow3TdTRjkdSvT-&index=2')
>>> q.xmth = 'random'
>>> q.to_img(800)

```

## Outputs

- [IjxkCokODEs](https://www.youtube.com/watch?v=IjxkCokODEs)

<img width="75%" src="./examples/pytci-ijxkcokodes-talk-to-her-zodiac-official-video.png"></img>

- [PVyS9JwtFoQ](https://www.youtube.com/watch?v=PVyS9JwtFoQ)

<img width="75%" src="./examples/pytci-pvys9jwtfoq-pixies-debaser-official-video.svg"></img>

- [D__UaR5MQao](pytci-d-uar5mqao-the-dp-3t-algorithm-for-contact-tracing-via-nicky-case.png) / [gxAaO2rsdIs](pytci-gxaao2rsdis-simulating-an-epidemic.png) / [Kas0tIxDvrg](pytci-kas0tixdvrg-exponential-growth-and-epidemics.png)

<img width="25%" src="./examples/pytci-d-uar5mqao-the-dp-3t-algorithm-for-contact-tracing-via-nicky-case.png"></img>
<img width="25%" src="./examples/pytci-gxaao2rsdis-simulating-an-epidemic.png"></img>
<img width="25%" src="./examples/pytci-kas0tixdvrg-exponential-growth-and-epidemics.png"></img>

## Copyright

2021 / D. COBAC / CC-BY-NC-SA
