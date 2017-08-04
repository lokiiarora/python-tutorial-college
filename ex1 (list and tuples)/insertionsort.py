def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp

list=[]
while True:
    n= raw_input("Enter a number: ")
    if n == 'end': break
    list.append(int(n))
print list
insertionsort(list)
print list