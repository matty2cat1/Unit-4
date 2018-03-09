#Matt westelman
#3/9/18
#functionDemo.py - how to use functions

def hw():
    print("hello, world")


def double(thingToDouble):
    print(thingToDouble * 2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)

def slope(x1, y1, x2, y2):
    print ((y2 - y1)/(x2 - x1))
    
slope(1,2,3,5)

double(False) #does this work

bigger(5,4)
bigger("Westelman","Matt")
