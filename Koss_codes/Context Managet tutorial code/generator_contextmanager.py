from contextlib import contextmanager
  
@contextmanager #decorator
def open_file(filename,mode):
    try:
        f = open(filename,mode)#file opened
        print("your file has been opened!")
       
        print("GRANTING U THE FILE TO WRITE")
        yield f 
        print("Did u close my file?")
    
    
    finally:
        f.close()
        print(f.closed)


with open_file("gentest.txt","w") as f:
    f.write("Yeah generator method to create context manager works fine too")

#NOTE:
# The yield keyword pauses generator function execution and the value of the 
# expression following the yield keyword is returned to the generator's 
# caller. It can be thought of as a generator-based version of the return 
# keyword. A yield , which causes the generator to once again pause and 
# return the generator's new value.

# decorator is analogically equivalent to append method of list for a
# function or class. it wraps new defined function as a method to class. 
