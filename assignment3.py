#Assignment 3
import csv
import argparse
import re
import urllib2



parse = argparse.ArgumentParser()
url_parser.add_argument('--url')
args = parser.parse_args()

def main():
	def dlData(url):
		file = urllib2.urlopen(url)
		return file

def process(data):
	data= csv.reader(data)
	images = 0
	hits= 0

	ie= 0
	firefox= 0
	safari= 0
	chrome = 0

	for row in data:
		label = row[0]
		browser = row[2]
		hits += 1

		the_images = (re.search(r'.gif$|.png$|.jpg$|.jpeg$',row[0],re.I,re.M))
		if the_images:
			images += 1
		else:
			continue


		the_ie = re.findall('MSIE\s', browser, re.I)
		the_chrome = re.findall('chrome/\d+', browser, re.I)	
		the_safari = re.findall('safari/\d+', browser, re.I)
		the_firefox = re.findall('firefox/\d+', browser, re.I)


		if the_chrome:
		chrome += 1
		elif the_ie:
		ie += 1
		elif the_firefox:
		firefox += 1
		elif the_safari:
		safari += 1

		browser= {'Safari': safari, 'Chrome':chrome, 'Firefox': firefox, 'MSIE':ie}
		
		print 'Image requests are {}% of all requests'.format(images*100/hits)
		print 'Most popular browser: 'max(browser, key=browser.get)
		





