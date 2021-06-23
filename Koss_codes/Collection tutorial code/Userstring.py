from collections import UserString
   
  
# Creating a custom char match string that is mutable
class Mystring(UserString):
    def append(self, s):# Function to append to string
        self.data += s
    def match_char(self, i, s):# Function to match charecter 
        return self.data[i] == s
    def remove(self, s):# Function to rmeove from
        self.data = self.data.replace(s, "")
      

s1 = Mystring("This is the last container ")
print("Original String:", s1.data)
  
# Appending to string
s1.append("known as userslists")
print("String After Appending:", s1.data)
  
# Removing from string
s1.remove("s")
print("String after Removing:", s1.data)
#matching the first charecter
print("Is the first charecter of above string 'T'?")
print(s1.match_char(0,"T"))