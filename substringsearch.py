import re
str=raw_input("Enter a string: ")
sub = raw_input("Enter the substring: ")
index = 0
count= 0
while index < len(str):        
    index = str.find(sub, index)     
    if index == -1:        
	break
    print "%s found at %d" % (sub , index)
    index += len(sub)
    count+=1
print "Total count = %d" % count
