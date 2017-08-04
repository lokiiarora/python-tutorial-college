import sys

# Not sure of the output , pls fix

def printthepattern(x):
    for y in range(0,x):
        for frontspace in range(0,2*(y)):
	    sys.stdout.write("\\")
	for pattern in range(0,2*(x-y-1)):
	    sys.stdout.write("!!")
	for endspace in range(0,2*y):
	    sys.stdout.write("\\")
	print(" ")

x=int(input("Enter the size:"))
printthepattern(x)
