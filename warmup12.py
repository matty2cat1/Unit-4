#Matt Westelman
#warmup12.py - pretty warm now!
#3/29/18

def gcf(x,y):
    i=x
    while i <= x:
        if x%i == 0 and y%i == 0:
                print(i)
                break
        else:
            i=i-1
       
gcf(12,15)
gcf(5,9)
gcf(16,64)
