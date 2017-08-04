import math
class Time:
    hours=0
    minutes=0
    seconds=0
    def __init__(self):
        self.hours=0
        self.minutes=0
        self.seconds=0
    def input_values(self):
        self.hours=int(raw_input("Enter hours? "))
        self.minutes=int(raw_input("Enter minutes? "))
        self.seconds=int(raw_input("Enter seconds? "))
    
    def print_values(self):
        print "Hours: %d \nMinutes: %d\nSeconds: %d" % (self.hours , self.minutes, self.seconds)
    
    def __add__(self,other):
        dummy = Time()
        dummy.hours = self.hours + other.hours
        dummy.minutes = self.hours + other.hours
        if(dummy.minutes>=60): 
            dummy.minutes-=60
            dummy.hours+=1
        dummy.seconds = self.hours + other.hours
        if(dummy.seconds>=60):
            dummy.seconds-=60
            dummy.minutes+=1
            if(dummy.minutes==60):
                dummy.minutes-=60
                dummy.hours+=1
        return dummy
    
    def __sub__(self,other):
        dummy=Time()
        h1,m1,s1 = self.hours, self.minutes , self.seconds 
        h2,m2,s2 = other.hours , other.minutes , other.seconds
        t1 = h1*60*60 + m1*60 + s1
        t2 = h2*60*60 + m2*60 + s2
        t3 = math.fabs(t2-t1)
        h3 = t3%60
        m3 = (t3/60) % 60
        s3 = (t3/60) % 60
        dummy.hours , dummy.minutes , dummy.seconds = h3 , m3 , s3
        return dummy
t1 = Time()
t1.input_values()
t2= Time()
t2.input_values()
t3 = t1 + t2
t3.print_values()
t4 = t1 - t2
t4.print_values()