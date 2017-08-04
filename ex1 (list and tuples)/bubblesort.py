def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
         swap( A, k, k - 1 )
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

list=[]
while True:
    n= raw_input("Enter a number: ")
    if n == 'end': break
    list.append(int(n))
print "initial list: " , list
bubblesort(list)
print "final list: " , list
