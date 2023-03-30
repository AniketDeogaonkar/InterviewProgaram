import time

def fiboitr(n):
    prevNum=0
    currentNum=1
    for i in range(1,n):
        prevPrevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevPrevNum
    return currentNum
        
        
def fiborecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiborecur(n-1) + fiborecur(n-2)
    
    
    

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    init = time.time()
    
    print(f"Using the recursion value of fib({num}) is {fiborecur(num)}")
    print(f"Using the Iterasation value of fib({num}) is {fiboitr(num)}")
    print(f"It tooks { time.time() - init} seconds")   #here to calculate the run time 
    