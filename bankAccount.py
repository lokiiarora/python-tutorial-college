class Bank_Account:
    acc_id=0
    name=""
    bal=0
    def __init__(self):
        pass
    def input_values(self):
        self.acc_id=int(raw_input("Enter Account ID? "))
        self.name=raw_input("Enter Account Holder's Name? ")
        self.bal=float(raw_input("Enter balance in the Account? "))
    def print_values(self):
        print "Account ID: ", self.acc_id
        print "Account Holder's Name: ", self.name
        print "Balance in the Account: ", self.bal
    def computeDraftLimit(self):
        return self.bal*0.9
class Current_Account(Bank_Account):
    def __init__(self):
        Bank_Account.__init__(self)
    def computeDraftLimit(self):
        return self.bal*1.2
c= Current_Account()
c.input_values()
print "Details in current account are :"
c.print_values()
print "The Draft Limit is: ", c.computeDraftLimit()
b= Bank_Account()
b.input_values()
print "Details in normal account are :"
b.print_values()
print "The Draft Limit is: ", b.computeDraftLimit()
