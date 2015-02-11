#!/usr/bin/python
#coding=utf-8
# ColorTheme资源分类脚本
# ./classify.py res目录
#目录下要分drawable-xhdpi drawable-xxhdpi等资源目录
#  将目录中的资源按照资源名字分别存放到对应的目录下
import sys
import os
import shutil

def mkdir(filepath):
	isExist = os.path.exists(filepath)
	if not isExist:
		os.makedirs(filepath)
	else:
		print filepath+' 目录已存在'


def	classify(dirname,colorname,sources):
	
	dpifile = []
	dpifile.append('drawable-xhdpi')
	dpifile.append('drawable-xxhdpi')
	dpifile.append('drawable-440dpi')
	dpifile.append('drawable-640dpi')

#	filepath = os.path.abspath(sys.argv[1])+'/'+dirname) #+'/drawable-xxhdpi')
	for dpi in dpifile:
		filepath = os.path.abspath(dirname+'/res/'+dpi)
		mkdir(filepath)
		for targetfile in sources:
	    		if dpi in targetfile:
					if colorname in targetfile:
						print targetfile
						moveFileto(targetfile,filepath)

def GetFile(dirpath):
    files = []
    for rootdir, dirs, filenames in os.walk(dirpath):
        for f in filenames:
            s = os.path.join(rootdir, f)
	    files.append(s)
    #return files
	path = os.getcwd()
	parent_path = os.path.dirname(sys.argv[1])
	print parent_path
    classify(parent_path+'/ColorTheme-Chocolate','chocolate',files)
    classify(parent_path+'/ColorTheme-Coral','coral',files)
    classify(parent_path+'/ColorTheme-DodgerBlue','dodgerblue',files)
    classify(parent_path+'/ColorTheme-LimeGreen','limegreen',files)
    classify(parent_path+'/ColorTheme-Tomato','tomato',files)
    classify(parent_path+'/ColorTheme-FireBrick','firebrick',files)
#    mkdir('ColorTheme-ForestGreen',files)i
#	mkdir('ColorTheme-Peru',files)

def moveFileto(sourceDir,  targetDir): 
	shutil.copy(sourceDir,  targetDir)
	os.remove(sourceDir)
	

if __name__ == "__main__":
	print GetFile(os.path.abspath(sys.argv[1]))
