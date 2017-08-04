import math

def conv(angle):
    return angle/57.2957795

def find(side1,side2,angle):
    return math.sqrt(math.pow(side1,2)+ math.pow(side2,2) - 2*side1*side2*math.cos(conv(angle)))

side1=float(input("Enter side 1:"))
side2=float(input("Enter side 2:"))
angle=float(input("Enter angle (in degrees):"))
print "The third side is %d" % (find(side1,side2,angle))
