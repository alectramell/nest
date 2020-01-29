import os
import sys
import urllib.request

def connect(host='http://www.google.com'):

	try:
		urllib.request.urlopen(host)
		return True
	except:
		return False

def runTrue():

        from urllib.request import urlopen
        print(urlopen('https://raw.githubusercontent.com/alectramell/beacons/master/colors.sh').read())

def runFalse():

        print('NO NETWORK CONNECTION..')

print(runTrue() if connect() else runFalse())
