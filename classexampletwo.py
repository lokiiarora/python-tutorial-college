class UG:
    level=""
    name=""
    regno=""
    def __init__(self,l,n,r):
        self.level,self.name,self.regno = l,n,r
    def print_val(self):
        print "He/She is in" , self.level
        print "He/She's name is " , self.name
        print "Registration Number is ", self.regno

class PG:
    level=""
    name=""
    regno=""
    def __init__(self,l,n,r):
        self.level,self.name,self.regno = l,n,r
    def print_val(self):
        print "He/She is in" , self.level
        print "He/She's name is " , self.name
        print "Registration Number is ", self.regno

def facMethod():
    choice=raw_input("Enter level he is in (UG/PG) ? ")
    name=raw_input("Enter name? ")
    reg=raw_input("Enter registration number? ")
    if choice=="UG": 
        obj= UG("UG", name,reg)
        obj.print_val()
    elif choice=="PG": 
        obj= PG("PG", name, reg)
        obj.print_val()
    else: print "Wrong choice"

facMethod()
    