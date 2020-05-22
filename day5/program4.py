#https://www.linkedin.com/in/piyushkumar0/

def knapSack(ksw, wt, val, n): 
  
    if n == 0 or ksw == 0 : 
        return 0

    if (wt[n-1] > ksw): 
        return knapSack(ksw, wt, val, n-1) 

    else: 
        return max( 
            val[n-1] + knapSack( 
                ksw-wt[n-1], wt, val, n-1),  
                knapSack(ksw, wt, val, n-1)) 


num = int(input("Enter number of items: "))
val = []
wt = []

for i in range(num):
    val.append(int(input("Enter value of item " + str(i+1) + " : ")))
    wt.append(int(input("Enter weight of item " + str(i+1) + " : ")))

ksw = int(input("Enter size of knapsack: "))

print("Total value of knapsack :", knapsack(ksw, wt, val, num)) 
