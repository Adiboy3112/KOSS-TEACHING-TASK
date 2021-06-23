from collections import Counter

#An dictionary with integer keys of alphabet A B C
Dict = {1: 'B', 2: 'B', 3: 'B', 4: 'B', 5: 'B', 6: 'A' , 7: 'A' , 8: 'A' ,9: 'C' , 10: 'C'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

print("To find the count of values in above Dictionary")
print("We can create counters in 3 ways")

# With sequence of items
print("1st method")
coun = Counter()
coun.update(['B','B','A','B','C','A','B','B','A','C'])
print(coun)

# with dictionary
print("2nd method") 
print(Counter({'A':3, 'B':5, 'C':2}))
    
# with keyword arguments
print("3rd method") 
print(Counter(A=3, B=5, C=2))