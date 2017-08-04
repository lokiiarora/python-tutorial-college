import random
def constructlist(namelist):
    for i in range(0,len(namelist)):
	dummydict={}
	temp={}
	for j in range(0,len(namelist)):
	    if namelist[i]!=namelist[j]: temp = {namelist[j]: random.randint(0,5)}
	    dummydict.update(temp)
	temp={}
	dictlist.append(dummydict)

def maxRating(namelist,dictlist):
    for i in range(0,len(namelist)):
        temp = [[k,v] for k,v in dictlist[i].items()]
	for [key, value] in temp:
	    ratinglist[namelist.index(key)]+=value
    max=""
    maxCount=0
    for i in range(0,len(namelist)):
	if(maxCount<ratinglist[i]):
	    maxCount=ratinglist[i]
	    max=namelist[i]
    if max: return max
    else: return "Everyone is the same" 

namelist=[]
dictlist=[]
ratinglist=[]
n=int(raw_input("Enter the number of people? "))
for i in range(0,n):
    name=raw_input("Enter name? ")
    namelist.append(name)
    ratinglist.append(0)
constructlist(namelist)
max = maxRating(namelist,dictlist)
print "Most popular friend is: " , max
