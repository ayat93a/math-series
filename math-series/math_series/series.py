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

