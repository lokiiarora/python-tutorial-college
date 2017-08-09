print "Trying to divide by zero"
try:
    z=5/0
except ZeroDivisionError:
    print "Caught the error gracefully"
finally:
    print "Can't divide by zero"