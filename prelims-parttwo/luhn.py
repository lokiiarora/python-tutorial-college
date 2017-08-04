
def appendtolist(num,index):
    x=num*2
    if(index%2!=0):
        list.append(num)
    elif(index%2==0):
        if(x<9):
            list.append(num)
        else:
            list.append(x%10)
            x=x//10
            list.append(x)
list=[]
index=0
num=int(input("Enter the credit card number: "))
if(len(str(num))!=16):
    print "Not a valid cradit card number"
else:
    for digit in map(int, str(num)):
        appendtolist(digit,index)
        index+=1
    if(sum(list)%10==0):
        print "Valid Credit card number"
    else:
        print "Invalid Credit Card Number"