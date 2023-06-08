"""Create a dictionary of a person that contains key value pair of
name: str
age: int
profession: str
married: bool
Set values with valid data types to each keys of the dictionary
Print the value of 'name' from the dictionary
Add the age by 10 and print the dictionary items in formatted string Eg: {name} will be {new_age} after 10 years.
Try getting the value of 'employed' from the dictionary.
If exception occurs, note it and check what exception says and finally comment the line.
try using get() method instead of large brackets [] in the previous question.
try using get() method with second parameter as False and see what is printed. Exa"""

person = {'name': 'poudel',
'age': 16 ,
'profession': 'python_developer',
'married': bool}
# Print the value of 'name' from the dictionary
print(person['name'])                              # poudel

#Add the age by 10 and print the dictionary items in formatted string Eg: {name} will be {new_age} after 10 years.
new_age = person['age'] + 10
print(f"{person ['name']} will be {new_age} after 10 years.")   #poudel will be 26 after 10 years.

#Try getting the value of 'employed' from the dictionary.
#emplyed = person['emplyed']
#print(person['employed'])                          #KeyError: 'employed'

#try using get() method instead of large brackets [] in the previous question.#
#employed = person.get(['emplyed']) 
#print(employed)                            #TypeError: unhashable type: 'list'

#try using get() method with second parameter as False and see what is printed. Exa"""
#employed = person.get['emplyed',False]
#print(employed)   


                 