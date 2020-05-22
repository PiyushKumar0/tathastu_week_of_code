#https://www.linkedin.com/in/piyushkumar0/

def sort(List):
    odd = []
    even = []
    for x in List:
        if x % 2 == 0:
            even.append(x)
        else :
            odd.append(x)
    return sorted(odd, reverse = True) + sorted(even)
    
size = int(input("Enter size of array: "))
li = []
for i in range(size):
    li.append(int(input("Enter element number " + str(i + 1) + " : ")))
print("Sorted array:", sort(li))
