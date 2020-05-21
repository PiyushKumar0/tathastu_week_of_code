#https://www.linkedin.com/in/piyushkumar0/

size = int(input("Enter size of tuple: "))
print("Enter elements in tuple")
a = []
for i in range(size):
    a.append(input())
a = tuple(a)
n = input("Enter the element whose number of occurences is to be found: ")
print("Number of occurences of",n,"in the tuple is:", a.count(n))
