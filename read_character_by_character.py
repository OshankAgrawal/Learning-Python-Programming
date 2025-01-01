l=["We are the students of AIADS branch.\n","This is Python lab.\n","In this lab we learn python programming.\n","and also run the programs to built our concepts\n"]

file = open("myfile.txt","w")
file.writelines(l)
file.close()

count_char = 0

file1 = open("myfile.txt","r")

reader = file1.readlines()
print("Character in file...")
for i in reader:
    for j in i:
        count_char += 1
        print(j)
print("Number of character in file is ",count_char)

