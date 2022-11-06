import Augmentor
import os
l=['bowling','catch','cover drive','dive','flick','pull shot','scoop shot','square cut','straight drive','sweep']
for i in l:
	path="data/train/"+i
	c=int(len(os.listdir(path)))
	print(c)
	p = Augmentor.Pipeline(path)
	p.flip_left_right(0.45)
	p.black_and_white(0.1)
	p.rotate(0.35, 25, 25)
	p.skew(0.15, 0.35)
	p.zoom(probability = 0.25, min_factor = 1.25, max_factor = 1.55)
	p.sample((225-c))