#!/usr/bin/python2.7

import requests
import json
import re
import datetime

r = requests.get("https://www.instagram.com/heycharlieitscooper/")

text = "\"followed_by\""

for line in r:
	if text in line:
	 	data = line


try:	
	count = re.search('"followed_by": {"count":\s(\d*)}' ,data).group(1) 
except NameError:
	sys.exit(0)
except:
	sys.exit(0)

time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

print time + ","  +count

today = datetime.datetime.now().strftime("%Y%m%d")

with open (today + "-stats.txt","a") as stats:
	stats.write(time + "," + count + "\n")

