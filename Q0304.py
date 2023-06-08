#Q0304
tuple = (10, 11, 12, 13, 14, 15)
print("the list of tuple with 5 different number is:",tuple)  #the list of tuple with 5 different number is: (10, 11, 12, 13, 14, 15)
tuple_2 = len(tuple)
print("the length of tuple is:" ,tuple_2)    #6
third_element = tuple[2]
print("third element of the tuple is:",third_element)    #13


# Create a tuple with 5 different numbers
my_tuple = (12, 45, 78, 33, 92)

# Find the length of the tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# Access the 3rd element of the tuple
third_element = my_tuple[2]
print("3rd element of the tuple:", third_element)

# Use enumerate() map 
for index, element in enumerate(my_tuple):
    print("Index:", index, "Element:", element)













"""
Quiz Q0304
Write a program to create a tuple to add 5 different numbers.
find out the length of the tuple
find out the 3rd element of the tuple by accessing it through the index
use enumerate() function to map each element with its index and print it using for loop.


"""