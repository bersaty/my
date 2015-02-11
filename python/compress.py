#!/usr/bin/python
#coding=utf-8
# 使用前请备份一份资源图片，这个工具会将压缩后的图片强制覆盖原来的
# 使用方法： 这个脚本和pngquant工具放在同一目录，执行： $./compress.py 资源文件夹/
# 
import os
import sys
import shutil
#os.system("ll")
#os.system("./pngquant --quality=50 --force ")


def Compress(filename):
    cmd = "./pngquant --quality=50 --force --skip-if-larger "+filename
    os.system(cmd)

def GetFile(dirpath):
    files = []
    for rootdir, dirs, filenames in os.walk(dirpath):
        for f in filenames:
            s = os.path.join(rootdir, f)
            files.append(s)
    for targetfile in files:
        Compress(targetfile)

if __name__ == "__main__":
    GetFile(os.path.abspath(sys.argv[1]))
