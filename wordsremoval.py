import os
from collections import Counter
import re
stopw=open("assets/stopwords.txt", 'r+')
stopwlines = stopw.readlines()
for index in range(0, len(stopwlines)):
    stopwlines[index] = stopwlines[index].strip()
stopw.close()
bookw=open("assets/book.txt", 'r+')
bookwlines= bookw.readlines()
for index in range(0, len(bookwlines)):
    bookwlines[index] = bookwlines[index].strip()
bookex=open("assets/book.save.txt", 'w+')
bookw.close()
for bline in bookwlines:
    for sline in stopwlines:
        bline=bline.replace(sline,"")
    bookex.write(bline)
bookex.close()
choice=raw_input("Do you want to replace words in stopwords.txt in book.txt (Yes/No)?")
if(choice == 'Yes' or choice =='yes' or choice=='YES'):
    os.remove("assets/book.txt")
    os.rename("assets/book.save.txt","assets/book.txt")
else:
    os.remove("assets/book.save.txt")
vocab=open("assets/vocab.txt","w+")
vocabdlines=vocab.readlines()
vocab.close()
for index in range(0, len(vocabdlines)):
    vocabdlines[index] = vocabdlines[index].strip()
words= re.findall(r'\w+', open('assets/book.txt').read().lower())
wordlist= Counter(words).most_common(100)
freqlist=[]
notexistinglist=[]
for word in vocabdlines:
    for (one,freq) in wordlist:
        if word==one : 
            freqlist.append(freq)
            break
print "The frequency list is:"
for index in range(0,len(vocabdlines)):
    print "%s:%d" % (vocabdlines[index],freqlist[index])
for (one,freq) in wordlist:
    existingbool=False
    for word in vocabdlines:
        if word==one:
            existingbool=True
            break
    if not existingbool: notexistinglist.append(one)
print "The words that do not exist in book.txt and exist in vocab.txt are: " , notexistinglist
choicenext=raw_input("Do you want to add these words to vocab.txt (Yes/No) ?")
vocab=open("assets/vocab.txt", 'a')
if (choicenext=='Yes' or choicenext=='yes' or choicenext== 'YES'):
    for word in notexistinglist:
        vocab.write(word+"\n")
vocab.close()
print open("assets/vocab.txt",'r+').readlines()