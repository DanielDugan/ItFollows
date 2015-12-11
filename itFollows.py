import urllib
from BeautifulSoup import*
import re

x=raw_input("Enter URL: ")
y=int(raw_input("Enter count: "))
z=int(raw_input("Enter position: "))

for turn in range(y+1):
    html=urllib.urlopen(x).read()
    soup=BeautifulSoup(html)
    tags=soup("li")
    count=0
    url2=""
    for tag in tags:
        count+=1
        if count!=z:
            continue
        url1=re.findall("https.+html",str(tag))
        x=str(url1)
        x=x.replace("['https","https")
        x=x.replace("html']","html")
        print ("Retrieving: "+ x )
