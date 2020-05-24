#https://www.linkedin.com/in/piyushkumar0/

import math 
  
def countdigits(N): 
    count = 0; 
    while (N): 
        count = count + 1; 
        N = int(math.floor(N / 10)); 
    return count; 
      
def cyclic(N): 
    num = N;
    n = countdigits(N); 
    
    rem = num % 10; 
    div = math.floor(num / 10); 
    num = ((math.pow(10, n - 1)) * rem + div)
    large = num
    
    while (1): 

        rem = num % 10; 
        div = math.floor(num / 10); 
        num = ((math.pow(10, n - 1)) * rem + div)
        
        if(num > N and num < large):
            large = num
          
        if (num == N): 
            break;  
              
    if(large == N):
        print("There is no number larger than", N)
    else:
        print("The next larger number than",N,"is",large)
        
num = int(input("Enter a number: "))
cyclic(num)
