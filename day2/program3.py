#https://www.linkedin.com/in/piyushkumar0

n = int(input("Enter the value of N: "))

print("\n")

for i in range(n):
    print(" " * i + "*" + "  " * (n - 1 - i) + "*")

for i in range(n):
    print(" " * (n - 1 - i) + "*" + "  " * i + "*")
