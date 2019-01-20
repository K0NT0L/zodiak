 #!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
# Recode? Tinggal pakai apa susahnya
# python simpel ;v
# W bikinnya Karna Gabut gan  ;v
# Coded by??? 
"""

import os
import json
from urllib2 import urlopen

Zodiak = """\033[1;37m
_____         _ _       _
|__  /___   __| (_) __ _| | __
  / // _ \ / _` | |/ _` | |/ /
 / /| (_) | (_| | | (_| |   <
/____\___/ \__,_|_|\__,_|_|\_\
      
 \033[1;38 Birth date and zodiac\033[1;36m V 1.1
"""
print Zodiak
name = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Name: ")
tgl = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Date: ")
bln = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Month: ")
thn = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Year: ")
url = "https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama="+name+"&tanggal="+tgl+"-"+bln+"-"+thn
dat = urlopen(url).read().decode("utf-8")
data = json.loads(dat)

print("\n\033[1;33m  { \033[1;37m*\033[1;33m } \033[1;37mInformation >>>\033[0m")
print "\033[1;33m  { \033[1;32m+\033[1;33m } \033[1;30mStatus\033[1;32m :\033[37m ", str(data['status'])
print "\033[1;33m  { \033[1;32m+\033[1;33m } \033[1;30mName\033[1;32m   :\033[37m ", str(data['data']['name'])
print "\033[1;33m  { \033[1;32m+\033[1;33m } \033[1;32m  :\033[37m ", str(data['data']['lahir'])
print "\033[1;33m  { \033[1;32m+\033[1;33m } \033[1;30mAge\033[1;32m   :\033[37m ", str(data['data']['usia'])
print "\033[1;33m  { \033[1;32m+\033[1;33m }\033[1;30mHBD\033[1;32m  :\033[37m ", str(data['data']['HBD'])
print "\033[1;33m  { \033[1;32m+\033[1;33m } \033[1;30mZodiak\033[1;32m :\033[37m ", str(data['data']['zodiak'])
os.system("exit")
    
