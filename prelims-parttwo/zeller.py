a=int(input("Enter the month of the year: "))
b=int(input("Enter the day of the month: "))
c=int(input("Enter the year of the century: "))
d=int(input("Enter the century: "))
if(a<=2):
    c=c-1
    a=a+10
w=(13*a-1)//5
x=c//4
y=d//4
z=w+x+y+b+c-2*d
r=z%7
if(r==0):
    print "Sunday"
elif(r==1):
    print "Monday"
elif(r==2):
    print "Tuesday"
elif(r==3):
    print "Wednesday"
elif(r==4):
    print "Thursday"
elif(r==5):
    print "Friday"
elif(r==6):
    print "Saturday"
