import os
import time
from threading import Thread
def pingcheck(counter,ip):
    counter+=1
    print "In thread no %d pinging %s" % (counter, ip)
    response=os.system("ping -c 1 " + ip)
    if response==0: print "%s is active" % ip
    else: print "%s is inactive" % ip
    print "Sleeping in 5 secs"
    time.sleep(5)

iplist=[]
counter=0
print "Enter the list of IPs you want to ping "
while True:
    dummy=raw_input()
    if dummy=="end": break
    iplist.append(dummy)
for ip in iplist:
    t= Thread(target=pingcheck, args=(counter,ip,))
    t.start()
