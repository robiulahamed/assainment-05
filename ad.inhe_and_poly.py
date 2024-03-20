import math
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    def __str__(self):
        return " this is a generic shape"
class  tirangle (shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        return 0.5 * self.b *self.h

    def parimeter(self):
        return 3 * self.b
    def __str__(self):
        return "this is trianngle wiht base {} and height {}".format(self.b, self.h) 
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side *self.side
    def perimeter(self):
        return 4 * self.side
    def __str__(self):
        return "this is squae wit side {}".format(self.side)

class ellipse(shape):
    def __init__ (self,m_a,mi_a):
        self.m_a=m_a
        self.mi_a=mi_a

    def area (self):
        return 3.14 * self.m_a * self.mi_a    

    def perimeter(self):
        h = ((self.m_a - self.mi_a) ** 2) / ((self.m_a + self.mi_a) ** 2)
        return math.pi * (self.m_a + self.mi_a) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))    

def print_info(s):
    print(str(s))
    print("Area:",s.area())
    print("permeteer: ",s.perimeter())
    print()

Triangle=tirangle(10,20)
Square=square(4)
Ellipse=ellipse(5,3)


print_info(Triangle)
print_info(Square)
print_info(Ellipse)