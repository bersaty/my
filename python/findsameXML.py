#!/usr/bin/python
#coding=utf-8

import os
import sys


def findsame(file):
	d={}
	for line in open(file):
		if 'name="' in line:
			name = line.split('"')[1]
			d[name] = d.get(name, 0) + 1 
#dict.get(key,default=None)a 对字典dict 中的键key,返回它对应的值value，如果字典中不存在此键，
#则返回default 的值(注意，参数default 的默认值为None) 
		#print d
	#fd = open('b.txt', 'w')
	for k, v in d.items():
		if v > 1: 
			#fd.write("sum:"+str(v)+" str:"+k)
			print("sum:   "+str(v)+" str:    "+k)
	#fd.close()

if __name__ == "__main__":
	findsame(os.path.abspath(sys.argv[1]))
	
