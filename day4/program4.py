#www.linkedin.com/in/piyushkumar0/
  
size = int(input("Enter number of items: "))
di = dict()

for i in range(size):
    key = input("Enter key for item " + str(i + 1) + " : ")
    di[key] = int(input("Enter the value for item " + str(i + 1) + " : "))

print("Originial dictionary:", di)

noDup = dict()

for key in di:
    if di[key] not in noDup.values():
        noDup[key] = di[key]

print("Dictonary after removing duplicate values:", noDup)
