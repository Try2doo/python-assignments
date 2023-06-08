"""
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee according to the customer's requirements.

The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user. Please use the function make_coffee() to prepare a coffee and serve it.

Followings are the ingredients for coffee:

Sugar: no. of spoons int
Beans: no. of spoons int
Milk: volume in ml. int
The total volume of coffee should be 250ml. The maximum volume of milk can be only up to 150ml. The volume Greater than the limit should give the error saying not acceptable.

Finally print the line describing the coffee you prepared along with milk and water composition.

"""

def make_coffee(sugar,beans,milk):
    if sugar >150:
        print("Erro: Milk volume exceeds the limits>please choose a small amount of it:")
        return
    
    water = 250 - milk
    



    print(f"the composition of the coffee with {sugar} spoon(s) of sugar, {beans}spone(s) of beans, and {milk} ml of milkz")
    print(f"the composition of the coffee is: {water} ml of water spoon(s) of sugar, {beans}spone(s) of beans, and {milk} ml of milkz")


sugar = input("enter number of sugar:")
spoon = input("enter number of spoon:")
milk = input("enter number of milk:")

1