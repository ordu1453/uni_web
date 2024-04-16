import math

class Chel():
    def __init__(self):
        self._weight = None
        self._color =None
        self._kind = None
        self._height = None
        
    def __repr__(self):
        return f"Человек весом:{self.weight}, ростом:{self.height}, пол:{self.kind}, с цветом кожи:{self.color}"
    
    def imt(self):
        l = self.weight/self.height
        if l>0.5:
            return "Zhirniy"
        elif l>0.3 and l<0.5:
            return "Ok"
        else:
            return "Drish"
    
def main():
    k = Chel()
    k.height = int(input("Height"))
    k.weight = int(input("Weight"))
    k.kind = str(input("Pol"))
    k.color = str(input("Color"))
    print(k)
    print(k.imt())
main();
