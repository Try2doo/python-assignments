"""

Write a python function that calculates the number of upper case characters, lower case characters and spaces in the string and returns them as a tuple.

For example: We have a string as "Hello World". The function should be able to return (2, 8, 1) where the first element is the count of Upper case characters, the second element is the count of lower case characters and third element is the count of spaces.


"""



def count_characters(string):
    uppercase_count = 0
    lowercase_count = 0
    space_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isspace():
            space_count += 1

    return (uppercase_count, lowercase_count, space_count)


text = "Hello World"
counts = count_characters(text)
print(counts)  # Output: (2, 8, 1)
