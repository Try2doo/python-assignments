#Quiz Q0302
#Write a program to add 5 different wild animals to a list named wild.
wild = ["tiger", "lion", "deer", "bear", "zebra"]   # copying from example
wild.sort()
print("Ascending  order of the wild animals is :",wild)      #['bear', 'deer', 'lion', 'tiger', 'zebra']

#now add 3 more animals to the list wild. Example: leopard, elephant, rhino
wild.append("leopard")
wild.append("elephant")
wild.append("rhino")
print(wild)    #['bear', 'deer', 'lion', 'tiger', 'zebra', 'leopard', 'elephant', 'rhino']

#or 
#wild.extend(["leopard","elephant","rhino"])
#print("afte 3 more animals add to the wild list is: ",wild)

#find the position of leopard using the index() method and remove it using the pop() method.
wild.index('leopard')
print('the index of the leopard is :',wild.index('leopard'))

a1 = wild.index('leopard')
wild.pop(a1)
print("final list of wild is :",wild )   #final list of wild is : ['bear', 'deer', 'lion', 'tiger', 'zebra', 'elephant', 'rhino']

wild.insert(2,"leopard")
print("Added the leopard in the wild list",wild)      # Added the leopard in the wild list ['bear', 'deer', 'leopard', 'lion', 'tiger', 'zebra', 'elephant', 'rhino']

#Remove rhino with remove() method:
wild.remove('rhino')
print("after removed the rhino is :",wild)        #after removed the rhino is : ['bear', 'deer', 'leopard', 'lion', 'tiger', 'zebra', 'elephant']

















