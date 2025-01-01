print("First of all you have to create a list.")

num = int(input("Enter the number of element in list."))

array = [0]*num
sum = 0
for i in range(0,num):
    print("Enter the value of ",i+1," element.")
    array[i] = int(input())

for j in range (0,num):
    a = min(array)
    b = max(array)

print("Smallest number in array is ",a,"Largest number in array is ",b)
