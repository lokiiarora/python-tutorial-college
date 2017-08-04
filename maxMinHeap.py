import heapq
listForTree = []
num=0
while True:
    n=raw_input("Enter a number? ")
    if n == 'end': break
    listForTree.append(n) 
listForMax= list(listForTree)
heapq.heapify(listForTree)
heapq._heapify_max(listForMax)
print "Min heap: " , listForTree        # for a min heap
print "Max heap: " , listForMax         # for a maxheap!!