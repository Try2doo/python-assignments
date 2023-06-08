
#Write a program to create an empty list named my_list
my_list = []
print(my_list)       # []

#Add numbers 5 and 9 to the list using append() method
my_list = []
my_list.append(5)
my_list.append(9)
print(my_list)        # [5,9]

#Ask the user to input any number in the console and add the number to the list.
#You can use int() to typecast string to integer if you want.

number = input("Enter_Your_Number:")
my_list.append(int(number))
print(f"Enter_your_Number{number} is {my_list}")   #[5, 9, 4]

#Create another list more_items with 3 items on it and extend the list my_list using extend method.
more_items = [7, 8, 9]
my_list.extend(more_items)
print(f"The list after extending with {more_items} is {my_list}")   
"""Enter_Your_Number:20
Enter_your_Number20 is [5, 9, 20]
The list after extending with [7, 8, 9] is [5, 9, 20, 7, 8, 9]
"""
#Now find the length of the list and print the length of list describing it in a sentence.
#you can use string formatting for better outputs.

print(f"Length of the list is {my_list.__len__()}")

#Now remove the second item using pop() method and see if the item exists in the list
#you can print the list before and after using the pop() method.
print("before pop second item:", my_list)
my_list.pop(1)
print("after pop second item:", my_list)











