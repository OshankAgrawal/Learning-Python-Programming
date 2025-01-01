num = int(input("Enter a number."))
if num <= 1:
    print("Neither prime nor composite")
c = 2
while c*c <= num:
    if num % c == 0:
        print("number is not prime")
        exit()
    c +=1
print("number is prime")