#Write a program to input a number from the terminal and check whether a number is an integer or not.
# integer = whole number ,positive number,without decimals etx 
# if number >= 0 or number <= 0 and number %1 == 0:
#print(f" Given no. {number:.2f} is Integer.")  
 #print(f" Given no. {number} is Integer.")   
# NOTE :negative decemial number not supported EGE  -5.5


 #Write a program to input a number from the terminal and check whether a number is an integer or not. 
x = (input('Enter your number: '))
number = float(x)
if number %1 == 0:
    print(" Given no. {} is Integer.".format(number))
else:    
     print(f"Input no. {number} is not a Integer.")




   













