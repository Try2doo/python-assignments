# hello krishna

#pattern 1
for x in range(1, 6):
    for j in range(x):
        print("* ", end=" ")
    print()

#pattern 2
for i in range(1,6):
    for j in range(i):
        print((2*j)+1,end=" ")
    print()
#pattern 3
for i in range(5):
    for j in range(i+1):
        print(1+i,end=" ")
    print()

#pattern 4
for i in range(6,-1,-1):
    for j in range(i+1):
        print(1+i,end=" ")
    print()

# Pattern 5
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="  ")
    print()

#pattern 6
word = "APPLE"
for i in range(len(word)):
    for j in range(i + 1):
        print(word[j], end=" ")
    print()


#pattern 7
for i in range(5):
    for j in range(5 - i):
        print("    ", end="")
    for k in range(i + 1):
        print("*   ", end="")
    print()


