# Set examples

st = ("HelloWorld", "for", "Welcome", "for.")
print(set(st))
print(len(st))

set1 = {1, 2, 3,3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set) # union combines two sets without duplication

set3 = {7, 8, 9}
set4 = {10,7,11,8}
my_set1 = set3.intersection(set4)
print(my_set1) # intersection returns common elements between two sets


set5 = {10, 20, 30}
set6 = {10, 45, 50, 20, 25}
my_set2 = set6.difference(set5)
print(my_set2) # difference returns elements in set5 that are not in set6
