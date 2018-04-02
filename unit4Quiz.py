#Matt Westelman
#4/2/18
#unit4Quiz.py

def count(a):
    i=0
    while i<a+1:
        print(i)
        i=i+1
count(4)

def excitedPrint(str):
    print(str.upper, '!!!')

excitedPrint('tasty')

def firstLetter(str):
    for ch in (str):
        return(ch)
        
print(firstLetter("bro"))

def repeats(e,f,g):
    if e==f or e ==g or f==g:
        return(True)
    else:
        return(False)
        
print(repeats(3,3,0))
