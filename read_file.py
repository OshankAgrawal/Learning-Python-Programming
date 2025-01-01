l=["We are the students of AIADS branch.\n","This is Python lab.\n","In this lab we learn python programming.\n","and also run the programs to built our concepts\n"]

file = open("myfile.txt","w")
file.writelines(l)
file.close()

file = open("myfile.txt","r")
print(file.read())