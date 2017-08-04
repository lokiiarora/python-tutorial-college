mtx=[]
n=int(raw_input("Enter the size of the matrix? "))
for i in range(0,n):
    dummy=[]
    for j in range(0,n):
        temp=int(raw_input("Enter a number? "))
        dummy.append(temp)
    mtx.append(dummy)
actualdict={}
dummydict={}
for i in range(0,n):
    for j in range(0,n):
        if mtx[i][j] !=0: 
            dummydict = {(i+1, j+1): mtx[i][j]}
            actualdict.update(dummydict)        
print actualdict