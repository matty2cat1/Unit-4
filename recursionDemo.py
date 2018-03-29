#Matt Westelman
#recursionDemo.py - recursive version of countdown
#3/29/18

def countdownr(n):
    if n == 0: #base case
        print('BOOM!') 
    else:
        print(n)
        countdownr(n-1)

countdownr(10)
