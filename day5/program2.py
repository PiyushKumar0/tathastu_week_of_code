#www.linkedin.com/in/piyushkumar0/

size = int(input("Enter size of array: "))
li = []
for i in range(size):
    li.append(int(input("\nEnter element " + str(i+1) + " : ")))
    
for i in range(size-1):
    li[i] = max(li[i+1:])
    
print("\nFinal array:", li)
