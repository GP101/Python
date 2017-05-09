#import sys
def fib(n):
    a,b = 0,1
    while a < n:
        #sys.stdout.write(str(a) )
        print a,
        a, b = b, a + b
    print " "
fib(100)