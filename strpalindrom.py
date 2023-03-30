import time 

str = input("Enter the string :")# take input from user 

palindrom=str[-1: :-1] # this is backword slicing , this slicing [StartPoint:EndPoint:Step]
if(str==palindrom):
    print("The String is Palindrom : ")
else:
    print("The String is Not Palindrom : ")

print(f"it took : {time.time()} second")