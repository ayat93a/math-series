# n = 'l'
# n = int(input('number'))
def fibonacci(n):
    try :
     if n <= 1:
        return n
     else:
        return fibonacci(n-1) + fibonacci(n-2)      
    except:
     print('fibonacci function accept only integer numbers')


"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
def lucas (n):
    try:
     if n <= 0:
        return 2
     elif n == 1:
        return 1
     else:
        return lucas(n-1) + lucas(n-2)
    except:
     print('lucas function accepts only integer number')

"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
def sum_series(n: int, base_0=0, base_1=1):
    try:
        if type(n) is not int or n < 0:
            raise TypeError("fibonacci and lucas functions accept only integer numbers")
        if n == 0:
            return base_0
        elif n == 1:
            return base_1
        else:
            return sum_series(n-1, base_0, base_1) + sum_series(n-2, base_0, base_1)
    except TypeError:
        return "not integer"
