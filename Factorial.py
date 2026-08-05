#factorial using recursion

def f(n):
    #base case
    if n==0 or n==1:
        return 1
    return( n*f(n-1) )
print(f(2))
print(f(3)) # 3*f(2)-->3*2*f(1)-->3*2*1  = 6
print(f(4)) # 4*f(3)-->4*3*f(2)-->4*3*2*f(1)-->4*3*2*1  = 24
