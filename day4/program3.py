#www.linkedin.com/in/piyushkumar0/

size = int(input("Enter size of dictionary: "))
di = dict()
for i in range(size):
    key = input("Enter key for item " + str(i + 1) + " : ")
    di[key] = int(input("Enter the value for item " + str(i + 1) + " : "))
    
print("Second largest value in Dictonary:", list(sorted(di.values()))[-2])
