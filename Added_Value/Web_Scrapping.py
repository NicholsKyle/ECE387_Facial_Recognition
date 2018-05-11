# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:30:56 2018

@author: Nicky
"""

from pynq import Overlay
import os
import http.cookiejar
import urllib.request
import requests
from bs4 import BeautifulSoup
import bs4

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

urllib.request.install_opener(opener)

authentication_url = "https://m.facebook.com/login.php"
payload = {
    # Our email and password has been removed for privacy reasons,
    # enter your Facebook email and password below to run the code
    'email':"",
    'pass':""
}
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
#print(contents)
url = "https://mbasic.facebook.com/groups/1753839841341777?view=members&status=100007953333548&stype=igcrs&_rdr"
data = requests.get(url, cookies=cj)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
soup=soup.find("div",{"id":"objects_container"})
#print(soup)
table=soup.findAll("table")
x=[]
base="https://mbasic.facebook.com"

#print(table)
for i in table:
    tds=soup.findAll("td",{"class":"r bq bm"})
    #print(tds)
    for j in tds:
        h3s=j.find("h3")
        #print(h3s)
        for a in h3s.findAll('a', href=True):
            #print ("Found the URL:", a.string)
            x.append([base+a['href'],a.string])
print(x)
for z in x:
    url=z[0]
    data = requests.get(url, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    prof=soup.find("div",{"id": "m-timeline-cover-section"})
    #pic=prof.find("div",{"class": "bl bm"})
    a=prof.find("a")
    url=base+a['href']
    #print(url)
    data = requests.get(url, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    soup=soup.find("div",{"id":"objects_container"})
    #print(soup)
    y=soup.findAll("div",{"class":"x"})
    print(y)
    image=soup.find("img")
    print(image)
    myPath='/home/xilinx/pynq/knownPeople/'
    fullfilename = os.path.join(myPath, z[1]+'.jpg')
    urllib.request.urlretrieve(image['src'], fullfilename)
    urllib.request.urlretrieve(image['src'],z[1]+'.jpg')
    

