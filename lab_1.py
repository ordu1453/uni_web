import sys
import math

def diskr(a,b,c):
  d = b*b-4*a*c
  return d

def quad(a,b,c):
  d = diskr(a,b,c)
  if a!=0 and d>=0:
    x1 = math.sqrt((-b+math.sqrt(d))/(2*a))
    x2 = -math.sqrt((-b-math.sqrt(d))/(2*a))
    x3 = math.sqrt((-b-math.sqrt(d))/(2*a))
    x4 = -math.sqrt((-b+math.sqrt(d))/(2*a))
    return x1,x2,x3,x4
  else:
    return 0
a = int(input("Enter a")
b = int(input("Enter b")
c = int(input("Enter c")

print(a,b,c)
print(diskr(a,b,c))
print(quad(a,b,c))

    
