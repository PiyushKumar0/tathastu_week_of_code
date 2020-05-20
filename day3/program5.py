#https://www.linkedin.com/in/piyushkumar0/

size1 = int(input("Enter no of elements in List 1: "))
print("Enter elements in List1")
list1 = []
for i in range(size1):
    list1.append(input())

size2 = int(input("Enter no of elements in List 2: "))
print("Enter elements in List2")
list2 = []
for i in range(size2):
    list2.append(input())

intersectList = list(set(list1).intersection(set(list2)))

print("Intersection of List 1 & List 2:", intersectList)
