#Matt Westelman
#distance.py
#3/30/18

from math import sqrt
def distance(a,b,c,d):
    return(sqrt((c-a)**2 + (d-b)**2))
    
print(distance(3,4,-5,2))
