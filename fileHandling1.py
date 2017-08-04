inputFileName= raw_input("Enter input file name that is full of comments? ")
outputFileName= raw_input("Enter the file name to output too? ")
try:
    inF= open(inputFileName,'r+')
    inlines = inF.readlines()
    inF.close()
    outF= open(outputFileName,'w+')
except (OSError, IOError,NameError) as e:
    print e
for line in inlines:
    if(line[0:1]=='#'): outF.write(line[1:])
    else: outF.write(line)
outF.close()