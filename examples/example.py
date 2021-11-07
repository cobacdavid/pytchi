import pytchi
import os


# 
o = pytchi.pytchi('https://www.youtube.com/watch?v=EelPrEojesM')
o.to_img() # export to png (concentric circles)
o.shape = 'lines'
o.to_img() # export to png (rectangle with lines)
#
p = pytchi.pytchi('https://www.youtube.com/watch?v=IjxkCokODEs')
p.offset = -300 # negative distance to the edges so that it zooms!
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
