class employee:
    da=0.0
    hra=0.0
    basic=0.0
    def __init__(self):
        self.da=0.0
        self.hra=0.0
        self.basic=0.0
    def inputval(self,da,hra,basic):
        self.da,self.hra,self.basic=da,hra,basic
    def salarycal(self,choice):
        if(choice=="salary"): return self.da+self.basic
        elif(choice=="gross"): return self.da+self.basic+self.hra
e= employee()
da=float(raw_input("Enter da? "))
hra=float(raw_input("Enter hra? "))
basic=float(raw_input("Enter basic pay? "))
e.inputval(da,hra,basic)
print "Salary is : " , e.salarycal("salary")
print "Gross Pay is : ", e.salarycal("gross")
