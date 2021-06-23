from sample_array import text
from collections import Counter
from collections import defaultdict

def def_value():
    return "Not Present"


count = Counter(text)
default_count = defaultdict(lambda: "Not Present",count)
#second arguement passed is initialization of default dict

#used context manager to write in file 
with open("task.txt","w") as f: 
	for k in count:
		f.write(k+": "+ str(count[k]) +"\n")
print("Is file closed?")
print(f.closed)
# Task 2:find count of various words in our default dict
print("Is 'happy'present in the database ?")
print(default_count['happy'])
print("How many 'unstructured' present ?")
print(default_count['unstructured'])
print("How many 'Aditya' present ?")
print(default_count['Aditya'])


