num = int(input("Enter the number."))
sum = 0
for i in range(num+1):
    sum = sum + i*i
print("Sum of squares of first ",num,"natural number is ",sum)