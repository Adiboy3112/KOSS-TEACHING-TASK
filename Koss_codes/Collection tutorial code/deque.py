from collections import deque 
lis = [1,2,3]
print ("The deque orignaly : ") 
print (lis)   

lis.remove(1) 
lis.remove(3) 
lis.insert(0,0)
lis.append(4)

print ("The list after operation is : ") 
print (lis)


# initializing deque 
de = deque([1,2,3])
print ("The deque orignaly : ") 
print (de)  

de.pop()#removes last element
de.popleft()#removes first element
de.append(4) # inserts 4 at the end of deque
de.appendleft(0) # inserts 0 at the beginning of deque  

print ("The deque after operation is : ") 
print (de)
