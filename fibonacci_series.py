num=int(input("Enter the number up to fibonacci series you want"))

def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(num+1):
    print(fibonacci(i))