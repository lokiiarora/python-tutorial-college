class Polygon:
    no_of_sides = 0
    sides = []

    def __init__(self,ns):
        self.no_of_sides=ns
    
    def input_sides(self):
        for i in range(0,self.no_of_sides):
            print "Enter side%d?" % (i+1)
            temp=int(raw_input())
            self.sides.append(temp)
    
    def print_sides(self):
        for i in range(0, self.no_of_sides):
            print "Side no%d = %d" % (i+1 , self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
        self.input_sides()
    def findArea(self):
        sum=0
        for i in range(0,self.no_of_sides): sum+=self.sides[i]
        return sum/2

t= Triangle()
print "Area is: %d" % (t.findArea())