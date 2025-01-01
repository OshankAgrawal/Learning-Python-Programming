def swap():
    num1 = int(input("Enter the value of first number."))
    num2 = int(input("Enter the value of second number."))
    num1,num2 = num2,num1
    print("After swaping the values\nValue of first number is ",num1,"\nValues of second number is ",num2)
swap()