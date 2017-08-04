def diff(x,y):
   if x<y:
      return y-x
   else:
      return x-y

x=int(input("Enter the price of book when bought at outlet or store:"))
y=int(input("Enter the average price of book if bought online:"))

print "Difference between store and online price = %d" % (diff(x,y))
