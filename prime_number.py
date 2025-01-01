def prime(num):
    i=2
    if num >1:
        for i in range(2,num+1):
            if num % i == 0:
                break
    elif num == 1:
        print("Entered number is",num,"\nIt is not a prime number.")
    else:
        print("Entere a correct number this number is not included in the category of Prime Number.")

    if num == i:
        print("Entered number is",num,"\nIt is a prime number.")
    else:
        print("Entered number is",num,"\nIt is not a prime number.")

num = int(input("Enter a number...."))
for i in range(0,num):
    prime(i)
