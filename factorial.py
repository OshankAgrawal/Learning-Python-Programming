def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
    
fact = 1
num = int(input("Enter a number for which you want to calculate factorial."))

print("Factorial of ",num,"is",factorial(num))