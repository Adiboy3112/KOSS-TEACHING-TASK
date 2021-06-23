from collections import namedtuple
#normal tuple
studenttuple = ('Aditya','16', '20EE10006')

# Declaring namedtuple() 
Student_namedtuple = namedtuple('Student',['name','section','rollno']) 
    
# Adding values 
S = Student_namedtuple('Aditya','16','20EE10006') 
    
# Access roll no from normal tuple 
print ("The Student rollno using tuple is : ",end ="") 
print (studenttuple[2]) 
    
# Access name from named tuple  
print ("The Student name using namedtuple is : ",end ="") 
print (S.name)