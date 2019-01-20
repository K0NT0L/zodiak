 #!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
# Recode? Tinggal make apa susahnya
# Di Kala Anda Bosan :v
# Coder by StarFuckTak
# Programer Tamvan;v
"""

import os
import json
from urllib2 import urlopen

Zodiak = """\033[1;33m
_____         _ _       _
|__  /___   __| (_) __ _| | __
  / // _ \ / _` | |/ _` | |/ /
 / /| (_) | (_| | | (_| |   <
/____\___/ \__,_|_|\__,_|_|\_\;
 _____________________________________________
 | Author : StarFuckTak\033[1;32m|\033[1;32m
 |Info :\033[1;32mZodiak\033[1;32|\033[1;32m
 |Version\033[1;32m 1.1\033[1;32m|033[1;32m
 ______________________________________________
 """
print Zodiak 
name = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Nama    : ")
tgl = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Tanggal : ")
bln = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Bulan   : ")
thn = raw_input("\033[1;32m  [\033[1;31m!\033[1;32m]\033[1;37m Tahun   : ")
url = "https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama="+name+"&tanggal="+tgl+"-"+bln+"-"+thn
dat = urlopen(url).read().decode("utf-8")
data = json.loads(dat)

print("\n\033[1;33m  [\033[1;37m*\033[1;33m] \033[1;37mInformation >>>\033[0m")
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mStatus\033[1;32m :\033[37m ", str(data['status'])
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mNama\033[1;32m   :\033[37m ", str(data['data']['nama'])
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mLahir\033[1;32m  :\033[37m ", str(data['data']['lahir'])
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mUsia\033[1;32m   :\033[37m ", str(data['data']['usia'])
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mUltah\033[1;32m  :\033[37m ", str(data['data']['ultah'])
print "\033[1;33m  [\033[1;32m•\033[1;33m] \033[1;30mZodiak\033[1;32m :\033[37m ", str(data['data']['zodiak'])
os.system("exit")
    
