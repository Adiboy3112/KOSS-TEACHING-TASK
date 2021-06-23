from collections import defaultdict 

# Defining the dict 
dd = defaultdict(int) 
#printing and empty defaultdict with key values that are not mapped
print("printing and empty defaultdict with key values that are not mapped")

for i in range(4):
    print(dd[i+1])
    # The default value is 0 
    # so there is no need to  
    # enter the key first 

L = [1, 2, 3, 4, 2, 4, 1, 2] 
 
for i in L: 
    dd[i] += 1
         
print(dd)





d ={}
#printing and empty dict with key values that are not mapped
print("printing and empty dict with key values that are not mapped")

for i in range(4):
    print(d[i+1])