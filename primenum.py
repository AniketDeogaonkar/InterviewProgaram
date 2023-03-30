num = int(input("Enter the Number : "))

for i in range(2, num):
    if num %i == 0:
        print(f"The {num} is Not Prime Number ")
        break
else:
    print(f"The {num} is Prime Number")
