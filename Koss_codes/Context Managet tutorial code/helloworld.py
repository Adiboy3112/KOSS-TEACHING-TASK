#manually opened the file then closed it after writing
f = open("test.txt","w")
f.write("hello world!")
#oops :( i forgot to close the file
print(f.closed)# showing status of file closure

#used python inbuilt context manager using "with" keyword 
with open("cmtest.txt","w") as f1:   
    data = f1.write("hello world!")
    #no need to close the file
print(f1.closed)# showing status of file closure