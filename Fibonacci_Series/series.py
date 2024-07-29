def fib(n):
    if n<=1:
        return n
    else:
        a=0
        b=1
        for i in range (2,n+1):
            sum=a+b
            a=b
            b=sum
    return b

print("Enter the number of iterations")
n=int(input())
res=fib(n)
print(f"The value in Fibonacci series for {n} iterations is {res}")
