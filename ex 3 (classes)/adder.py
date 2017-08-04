class Adder:
    def __init__(self,counter): 
        print "%dth instance created" % (counter+1)
    def listAdd(self,first,second):
        total = list(first)
        for i in range(0,len(second)):
            total.append(second[i])
        return total
    def dictAdd(self,first,second):
        total = first.copy()
        total.update(second)
        return total
counter = 0
a1= Adder(counter)
counter+=1
a2= Adder(counter)
counter+=1
a3= Adder(counter)
print "Adding two lists : [1,2,3] + [5,10,15] = ", a1.listAdd([1,2,3] , [5,10,15])
print "Adding two dictionaries : {1:1,2:1,3:3} + {5:5,10:10,15:15} = ", a2.dictAdd({1:1,2:1,3:3}, {5:5,10:10,15:15})