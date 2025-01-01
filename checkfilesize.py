l=["We are the students of AIADS branch.\n","This is Python lab.\n","In this lab we learn python programming.\n","and also run the programs to built our concepts\n"]

file = open("myfile.txt","w")
file.writelines(l)
file.close()

count_line = 0
count_char = 0

file1 = open("myfile.txt","r")

reader1 = file1.readlines()

for i in reader1:
    count_line +=1

    for j in i:
        count_char += 1

print("Lines in the file is ",count_line,"\nCharacter in file is ",count_char)
