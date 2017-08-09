import os 
print "Trying to change permissions to the file"
os.chmod("./classexample.py",0444)
try:
    dummy=open('./classexample.py','w+')
except IOError:
    print "The file is read only"
finally:
    print "This demonstrates that file permission has been changed"