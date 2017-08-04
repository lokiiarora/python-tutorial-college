import requests
import time
from threading import Thread

def urlFetch(i,url):
    i+=1
    print "In %dth thread , fetching %s" % ((i+1) , url)
    u=requests.get(url, stream=True)
    for chunk in u.iter_content(chunk_size=1024):
        print chunk
        break
    print "Sleeping in 2 seconds"
    time.sleep(2)

urllist = []
counter=0
print "Enter the list of URLs:"
while True:
    dummy=raw_input()
    if dummy=="end": break
    urllist.append(dummy)

for url in urllist:
    t= Thread(target=urlFetch, args=(counter,url,))
    t.start()