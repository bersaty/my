#!/usr/bin/python
#key 163:g19p7XC0mEUNZZJddzgOiWt0h08l3t-7
#key meizu:cgXDspGWjEjfIjxE_SzzomRKMfJrXvE5
#key gmail:Z2WY4Vk1ZqoCPCBaeYnvhCwyZL9vekov
# ./tinypng.py res-path


from os.path import dirname
from urllib.request import Request, urlopen
from base64 import b64encode
import os,sys

#key = "g19p7XC0mEUNZZJddzgOiWt0h08l3t-7"
#key = "cgXDspGWjEjfIjxE_SzzomRKMfJrXvE5"
key = "Z2WY4Vk1ZqoCPCBaeYnvhCwyZL9vekov"
#output = "teste/tiny-output.png"

def compressfile(inputfile,outputfile):
	output = sys.argv[1]+"/compressed/"+outputfile
	request = Request("https://api.tinypng.com/shrink", open(inputfile, "rb").read())

	cafile = None
	# Uncomment below if you have trouble validating our SSL certificate.
	# Download cacert.pem from: http://curl.haxx.se/ca/cacert.pem
	# cafile = dirname(__file__) + "/cacert.pem"

	auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
	request.add_header("Authorization", "Basic %s" % auth)

	response = urlopen(request, cafile = cafile)
	if response.status == 201:
	  # Compression was successful, retrieve output from Location header.
	  result = urlopen(response.getheader("Location"), cafile = cafile).read()
	  open(output, "wb").write(result)
	  print (output)
	else:
	  # Something went wrong! You can parse the JSON body for details.
	  print("Compression failed"+inputfile+"\n")


def mkcompressdir():
	filepath = os.path.abspath(sys.argv[1]+"/compressed")
	isExist = os.path.exists(filepath)
	if not isExist:
		os.makedirs(filepath)
	else:
		print (filepath+" is existed!!!")
	return True


def GetFile(dirpath):
	files = {}
	for rootdir, dirs, filenames in os.walk(dirpath):
		for f in filenames:
			s = os.path.join(rootdir, f)
			files[s] = f
	mkcompressdir()
	for (key1,targetfile) in files.items():
		compressfile(key1,targetfile)

if __name__ == "__main__":
	GetFile(os.path.abspath(sys.argv[1]))
	#inputfile = "large-input.png"
	#outputfile = "large-output.png"
	#compressfile(inputfile,outputfile)

