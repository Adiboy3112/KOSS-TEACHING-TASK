from collections import UserList 
# Creating a List where 
# deletion is not allowed 
class MyList(UserList):         
    # Function to stop deleltion from List 
    def remove(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
            
    # Function to stop pop from List 
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
         
UL = MyList([1, 2, 3, 4]) 
L = [1, 2, 3, 4]   
print("Original List")
print(L)
print("Original User List")
print(UL)
# Inserting to List" 
UL.append(5)
L.append(5)

print("After Insertion in list ") 
print(L) 
print("After Insertion in user list ") 
print(UL) 
print("Tryin to remove item from list")    
# Deliting From List 
L.remove(1)
print("Trying to remove item from user list")
UL.remove(1)# Deliting From userList 