
rich =  {"USA", "China", "Japan", "Germany", "France", "Australia", "Italy"}
europe =  {"Germany", "France", "England", "Switzerland", "Italy", "Portugal", "Sweden"}

#countries that are rich but not in Europe
rich_not_eup = rich - europe
print(f"countries that are rich but not in Europe:",rich_not_eup)  #{'Australia', 'China', 'USA', 'Japan'}

# countries that are in Europe but not rich
eup_not_rich = europe - rich
print("countries that are in Europe but not rich:",eup_not_rich)  #{'Switzerland', 'Portugal', 'Sweden', 'England'}

# countries that are both rich and are in Europe
eup_rich = europe | eup_not_rich 
print("countries that are both rich and are in Europe:", eup_rich)  #{'France', 'Germany', 'Italy'}

# countries that are either rich or in Europe, but not both
rich_and_eup = rich ^ europe   #.symmetric_difference
print("countries that are either rich or in Europe, but not both:",rich_and_eup)  # {'Japan', 'Portugal', 'Switzerland', 'Sweden', 'China', 'USA', 'Australia', 'England'}

#all the countries in either of the sets. (Names must be unique)
rich_and_eup_unique = rich | europe 
print("all the countries in either of the sets and Unique :",rich_and_eup_unique) # {'France', 'USA', 'England', 'Sweden', 'Japan', 'Switzerland', 'Australia', 'Italy', 'China', 'Germany', 'Portugal'}

#see if two sets are disjoint or not
disjoint = rich.isdisjoint(europe)
print("Is disjoint sets ?: ",disjoint)  #False

#Remov commo from rich
x = rich.difference_update(europe)
print(x)   #NONE

#Create 2 more sets:
rich = {"USA", "China", "Japan", "Germany", "France", "Australia", "Italy"}
asian_rich = {"China", "Japan"}
american_rich = {"USA", "Canada"}

#Check whether asian_rich is a subset of rich or not
subset_0 = asian_rich.issubset(rich)
print("Is asian_rich  subset of rich?", subset_0) # True

#Check whether rich is a superset of asian_rich or not.
subset_2 = rich <= asian_rich
print("whether rich superset of asian_rich :",subset_2)   # True

#Check whether american_rich is a subset of rich or not. Note: you can use different operators to perform above operations
subset_3 = american_rich >= rich
print(subset_3)   #false










