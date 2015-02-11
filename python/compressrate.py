#!/usr/bin/python
#coding=utf-8
#比较两个文件内体积大小
import sys
import os

files1 = {}
files2 = {}

def GetFile(filepath,files):
	for r,dn,fn in os.walk(filepath):
		for f in fn:
			s = os.path.join(r,f)
			size = os.path.getsize(s)
			files[f] = size
#	print files1
	return files;

def Compare():
	for (key,value) in files1.items():
		print str(value)+"   	"+str(files2[key])+"   	"+str(1-round(value*1.0/files2[key],4))+"		"+str(key)

if __name__ == "__main__":
	print "大小    大小    压缩率"
	files1 = GetFile(os.path.abspath(sys.argv[1]),files1)
	files2 = GetFile(os.path.abspath(sys.argv[2]),files2)
	Compare()
