print("First of all you have to create an Array.")

num = int(input("Enter the number of element in Array."))

array = [0]*num
sum = 0
for i in range(0,num):
    print("Enter the data of ",i+1,"th element.")
    array[i] = input(" ")

for j in range (0,num):
    sum = sum + int(array[j])

print("Sum of array is ",sum)