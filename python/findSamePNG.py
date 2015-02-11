#!/usr/bin/python
#coding=utf-8
# Usage: 
#   $./findSamePNG.py arg1 arg2
#   param arg1: 资源路径1
#   param arg2: 资源路径2
# Function:
#   使用MD5找两个文件夹内相同的png图片
#   在控制台输出，而且会生成一个SamePNGreport.html的报告，报告内容显示相同的图片和相对应的路径
# Author: OuGuiBin, Meizu SDK Team
# Date: 2014-9-6
#
# Modify: wuchunhui ,meizu SDK Team
# Date: 2014-12-19
import sys
import os
import hashlib

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        #print(hash)
        return hash     

def GetFileHashs(dirpath):
    filehashs = {}
    for rootdir, dirs, filenames in os.walk(dirpath):
        for f in filenames:
            s = os.path.join(rootdir, f)
            filehashs[s] = CalcMD5(s)
    return filehashs

#def GetFileHashsPNG(dirpath):
#    filehashs = {}
#    for rootdir, dirs, filenames in os.walk(dirpath):
#        for f in filenames:
            #if os.path.splitext[2]=='png':
#                s = os.path.join(rootdir, f)
#                filehashs[s] = CalcMD5(s)
#    return filehashs

def FindMatchFileHashs(hashs1, hashs2):
    match_count = 0
    for key1, value1 in hashs1.iteritems():
        for key2, value2 in hashs2.iteritems():
            if value1 == value2:
                match_count = match_count + 1
                print ("Match:   ", value1)
                print ("      file:    ", key1)
                print ("      file:    ", key2)
    return match_count

def FindMissMatchHashs(hashs1, hashs2):
    match_count = 0
    print ("相同的图片:\n")
    for key1, value1 in hashs1.iteritems():
        match = False;
        for key2, value2 in hashs2.iteritems():
            if value1 == value2:
                match = True
                #print value1+"=========="+value2
                print (key1+" ============ "+key2)
        if match==True:
            match_count = match_count + 1
    print ("\n")
    return match_count


def ReportHTML(hashs1, hashs2):
    #print "<!DOCTYPE HTML>\n<html>\n<body>\n"
    match_count = 0
    match_strings = []
    for key1, value1 in hashs1.iteritems():
        match = False;
        for key2, value2 in hashs2.iteritems():
            if value1 == value2:
                match = True;
                match_count = match_count + 1
                s = "<tr><th colspan=\"2\">res-path1</th><th colspan=\"2\">res-path2</th></tr>\n"
                s = s + "<tr>\n" + "  <td cellpadding=\"10\" >\n    <img src=\"" + key1 + "\" width=\"100\" height=\"100\" />\n  </td>\n" + "  <td cellpadding=\"10\" >" + key1 + "</td>" +"  <td cellpadding=\"10\" >\n    <img src=\"" + key2 + "\" width=\"100\" height=\"100\" />\n  </td>\n" + "  <td cellpadding=\"10\" >" + key2 + "</td>"+ "</tr>\n"
                match_strings.append(s)

        #if match==False:
            #match_count = match_count + 1
            #s = "<tr><th colspan=\"2\">" + value1 + "</th></tr>\n"
            #s = s + "<tr>\n" + "  <td cellpadding=\"10\" >\n    <img src=\"" + key1 + "\" width=\"100\" height=\"100\" />\n  </td>\n" + "  <td cellpadding=\"10\" >" + key1 + "</td>" + "</tr>\n"
            #match_strings.append(s)

    #print "<p>matches:", match_count, "</p>\n"
    #print "<table border=\"1\" style=\"table-layout:fixed;\">\n"
    #for s in match_strings:
        #print s;
    #print "</table>\n"
    match_strings.append("<!DOCTYPE HTML>\n<html>\n<body>\n</table>\n\n</body>\n</html>\n")
    f=file(os.path.abspath('.')+'/SamePNGreport.html','w+')
    f.writelines("<p>Matches:"+format(match_count)+"</p>\n\n\n<table border=\"1\">\n")
    f.writelines(match_strings)
    f.close() 
    #print "<p>Matches:",match_count,"</p>\n\n<table border=\"1\">\n"
    #print "<table border=\"1\">\n"
    #for s in match_strings:
        #print s;
    #print "</table>\n\n</body>\n</html>\n"

if __name__ == "__main__":
    #print sys.argv[1];
    #print sys.argv[2];
    fhs1 = GetFileHashs(os.path.abspath(sys.argv[1]))
    fhs2 = GetFileHashs(os.path.abspath(sys.argv[2]))
    #print FindMatchFileHashs(fhs1, fhs2), "Matches"
    print (FindMissMatchHashs(fhs1, fhs2), "matches")
    #print os.path.abspath('.')
    ReportHTML(fhs1, fhs2)
    

