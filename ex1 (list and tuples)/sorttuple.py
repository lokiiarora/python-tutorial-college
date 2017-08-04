from operator import itemgetter
def last(n):
    return n[-1]
list= []
while True:
    n= raw_input("Enter a tuple: ")
    if n == 'end': break
    list.append(tuple(map(int,n.split(','))))
print "List is: " , list
print "Sorted List is: " , sorted(list,key=last)

