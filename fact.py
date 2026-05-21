n=int(input("Enter the value"))
print("The value is",n)
Factorial=1
if n==0:
    print("Factorial of n is 1")
else:
    for i in range(1,n+1):
        Factorial*=i
    print("Factorial of",n,"is",Factorial)
