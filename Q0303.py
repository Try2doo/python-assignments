#Quiz Q0303

multi = [
    [12, 52, 37],
    [46, 51, 16],
    [17, 82, 39],
]
print(multi[1][1])     #51
print(multi[-1][-2])   #82

print(len(multi))     #3

x = [40, 61,10]
x = multi.append(x)
print(multi)

# 

multi.clear()
print("the FINAL list is: ", multi)