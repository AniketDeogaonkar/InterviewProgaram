import time

num = int(input("Enter the Number : "))

rev = 0
x = num

while (num>0):
    rev=(rev*10) + num % 10
    num=num//10
    
if(rev==x):
    print("The Number is Palindrom ")
else:
    print("The Number is Not Palindrom ")
    
print(f"it took : {time.time()} second")   

