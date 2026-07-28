#Recursion : a function calling itself to solve a problem
#           also for getting its prev. output from itself
#Fibonacci series 0 1 1 2 3 5 8 13 21 34 ...
 #                0 1 2 3 4 5 6 7  8  9 
#it is not define for negative number
"""
fib(0)=0 #base case
fib(1)=1 #base case
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(n)=fib(n-2)+fib(n-1)   for n=0 n=1 this function not holding value
"""
def fib(n):
    #base case is must
    if(n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)

print(fib(6))#8
#for solving fib(6)-->
#fib(5)+fib(4)
#fib(4)+fib(3)+fib(3)+fib(2)
#fib(3)+fib(2)+fib(2)+fib(1)+fib(2)+fib(1)+fib(1)+fib(0)
#fib(2)+fib(1)+fib(1)+fib(0)+fib(1)+fib(0)+fib(1)+fib(1)+fib(0)+fib(1)+fib(1)+fib(0)
#fib(1)+fib(0)+fib(1)+fib(1)+fib(0)+fib(1)++fib(1)+fib(0)+fib(1)+fib(0)+fib(1)+fib(1)+fib(0)
a= 1 +0+1+1+0+1+1+0+1+0+1+1+0
print(a)  