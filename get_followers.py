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
except:
	sys.exit(1)

time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

print time + ","  +count

with open ("stats.txt","a") as stats:
	stats.write(time + "," + count + "\n")
