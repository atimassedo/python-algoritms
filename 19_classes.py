class Fraction:
    def __init__(self,a,b):
        self.first = [int(i) for i in a.split("/")]
        self.second = [int(i) for i in b.split("/")]

    def summa(self):
        self.numerator = self.first[0] * self.second[1] + self.second[0] * self.first[1]
        self.delimentr = self.first[1] * self.second[1]
        return self.numerator / self.delimentr

    def multply(self):
        self.numerator = self.first[0] * self.second[0]
        self.delimentr = self.first[1] * self.second[1]
        return self.numerator/self.delimentr

    
    def div(self):
        self.numerator = self.first[0] * self.second[1]
        self.delimentr = self.first[1] * self.second[0]
        return self.numerator/self.delimentr
        



a = str(input())
b = str(input())


r = Fraction(a, b)
print(r.div())
print(r.summa())



    

    

        





    
    


    

    

    
        



