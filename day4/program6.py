#www.linkedin.com/in/piyushkumar0/
  
size = int(input("Enter size of dictonary: "))
di = []
for i in range(size):
    di.append(input("Enter word number " + str(i + 1) + ": "))

size = int(input("\nEnter size of array: "))
array = []
result = []

for i in range(size):
    array.append(input("Enter character number " + str(i + 1) + " in array: "))

for value in di: 
    if set(value).issubset(set(array)):
        result.append(value)

print("\n" + result)
