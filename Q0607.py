"""Convert the following loop to list comprehension
lst = []
for x in range(10):
    lst.append(2*x+1)
"""
#1 Convert the following loop to list comprehension

my_list =[2*x+1 for x in range(10)]

print(my_list)

#2 Generate a dictionary from a list of first 10 numbers and it's square values using dictionary comprehension.

#inal value should be similar to: {1:1, 2:4, 3:9, 4:16, ..., 10, 100}

for i in range(1,11):
    print(i,end=' ')
print()

#3 
n = list(range(1, 11))
dict = {num: num ** 2 for num in n}
print(dict)


#4

patt = '\n'.join([' '.join(map(str, range(1, i+1))) for i in range(1, 6)])
print(patt)





#5
def generate_y(start, end):
    for x in range(start, end):
        yield 4 * x ** 2 + 3 * x - 6

y_generator = generate_y(-100, -100 + 1000)
print(y_generator)
y_list = [4 * x ** 2 + 3 * x - 6 for x in range(-100, -100 + 1000)]
print(y_list)


