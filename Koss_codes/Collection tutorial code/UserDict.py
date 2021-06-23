from collections import UserDict
#plain dictionary
d={'a':1, 'b': 2, 'c': 3}
print("Original Dictionary")
print(d)
del d['a']
print("After deleting")
print(d)

# Creating a Dictionary where deletion is not allowed
class MyDict(UserDict):
    # Function to stop deleltion from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
          
    # Function to stop pop from dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
          
    # Function to stop popitem from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")
      
# Driver's code
ud = MyDict({'a':1, 'b': 2, 'c': 3})
  
print("Original  User-Dictionary")
print(ud)
  
ud.pop(1)
print(ud)