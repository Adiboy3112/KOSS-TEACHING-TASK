from collections import OrderedDict
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print('Before Deleting')
for key, value in d.items(): 
    print(key, value) 
# deleting element
del d['a']
# Re-inserting the same
d['a'] = 1
print('\nAfter re-inserting')
for key, value in d.items():
    print(key, value) 

print("\nThis is a ordered Dict:\n")
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
# deleting element
od.pop('a')
# Re-inserting the same
od['a'] = 1
print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)
