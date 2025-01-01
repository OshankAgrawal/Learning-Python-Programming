import sys
l=("We are the students of AIADS branch.","This is Python lab.","In this lab we learn python programming.","and also run the programs to built our concepts.")
a = sys.getsizeof(l)
b = str(l.__sizeof__())
print(a,"      ",b)
# The __sizeof__() method and the getsizeof() method both are used to get the
# size of the objects used in the program. The getsizeof() method returns 
# an additional overhead for garbage collection along with each element 
# size of the list. The __sizeof_() method returns the actual size of the 
# object without any overhead