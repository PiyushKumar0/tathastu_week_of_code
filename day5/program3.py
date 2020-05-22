#https://www.linkedin.com/in/piyushkumar0/

def max_loot(hval, n): 
	if n == 0: 
		return 0

	if n == 1: 
		return hval[0] 

	value2 = max(hval[0], hval[1]) 
	if n == 2: 
		return value2
		
	value1 = hval[0] 
	max_val = None

	for i in range(2, n): 
		max_val = max(hval[i]+value1, value2) 
		value1 = value2 
		value2 = max_val 

	return max_val 

size = int(input("Enter number of houses: "))
hval = []
for i in range(size):
    hval.append(int(input("Enter value of house " + str(i+1) + " : ")))

print("Maximum loot value :", max_loot(hval, size)) 
