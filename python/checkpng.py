#!/usr/bin/python
#coding=utf-8

import sys,os,Image
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator,FuncFormatter
import numpy as np

y = []

def getFile(dirpath):
	for rootdir,dirs,filename in os.walk(dirpath):
		for f in filename:
			s = os.path.join(rootdir,f)
			if ".png" in s:
				size = os.path.getsize(s)
				y.append(size)
				if size > 30000 :
					im = Image.open(s)
					pixels = im.size[0]*im.size[1]  #像素
					print "路径:"+s
					#print im.format,im.size,im.mode #im.info,str(im)
					print "像素:"+str(im.size)
					print "体积："+str(size/1024) + "K" #体积

if __name__ == "__main__":
	getFile(os.path.abspath(sys.argv[1]))
	pl.ylim(0.0,1000)
	y.sort()
	pl.plot(y)

	print "\n图片总数:"+str(len(y))
	#pl.show()
