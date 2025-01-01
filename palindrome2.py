num=(int(input("Enter any digit number.")))
num_org=num
count = 0
while num != 0 :
    count +=1
    num=num//10
    
list =[0]*count

num=num_org

for i in range(count):
    list[i]=num%10
    num=num//10
  
for i in range(count):
    print(list[i])
    
rev_num=0

for k in range(1,count+1):
    rev_num=rev_num+list[-k]*(10**(k-1))

if num_org==rev_num:
    print("Entered number is palindrome.")
else:
    print("Entered number is not a palindrome.")
