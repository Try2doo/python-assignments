"""Write a program that accepts a number from the terminal and 
checks whether it is a multiple of both 3,4, and 5 or not
"""
num =int(input("Enter your number: "))
if(num %3 == 0 and num %4 == 0 and num %5 == 0) :
    print(f"{num} is a multiple of both 3,4 and 5")
else:
    print(f"{num} is not a multiple of both 3,4 and 5")


    


