#warmup11.py - is the number prime?
#3/26/18
#Matt Westelman


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
print(prime(8))
print(prime(11))
print(prime(14))
