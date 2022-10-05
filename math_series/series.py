def fibonacci (n):
    # function that return nth value in fibonacii series
    if type(n) != int:
        return "Plz Enter a Number"
    if n < 0:
        return "Plz enter a positive number"      
    if n == 0:
        return 0
    elif n ==1 :
        n==1
        return 1
    else : 
        return fibonacci(n-1) + fibonacci(n-2)    


def lucas(n):
     
 #Return the nth number in the Lucas series.
    if type(n) != int:
        return "Plz Enter a Number"
    if n < 0:
        return "Plz enter a positive number"      
    if n == 0:
        return 2
    elif n ==1 :
        return 1
    else :
        return lucas(n-1)+lucas(n-2)    

def sum_series(n,x=0,y=1) :
    """ 
   Return the nth number in a series where the user decides the base arguments.
    If the optional arguments were not specified the function returns the nth number in the Fibonacci series
    """

    
    if type(n) != int:
        return "Plz Enter a Number"
    if n < 0:
        return "Plz enter a positive number" 

    if x ==0 and y == 1:
        return fibonacci(n)
    elif x==2  and y ==1 :
        return locals(n)

    elif n==0:
        return x
    elif n ==1 :
        return y


    else :
        return (sum_series(n-2, x=x, y=y) + sum_series(n-1, x=x, y=y))    


print("Fibonacci Series  5th position: ",fibonacci(5))
print("Fibonacci Series  -3th position: ",fibonacci(-3))
print("lucas Series  7th position: ",lucas(7))
print("lucas Series  -4th position: ",lucas(-4))
print("Sum Series  -5th position: ",sum_series(-5))
print("Sum Series  0th position: ",sum_series(0))
print("Sum Series  7th position: ",sum_series(7))
print("Sum Series  9th position: ",sum_series(9,4,5))






                

