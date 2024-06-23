my_dict = {'a' : 1, 'v' : 3, 'b' :2, 'c' : 5, 'd' : 4}
print(my_dict)

for i in my_dict.items():
    print(i)

for i, j in my_dict.items():
    print(i, j)

from collection import OrderdDict
my_dict = OrderedDict(my_dict)

# Dict is not sorted. it will not keep the order of insertion
# OrderedDict - it will keep the order of insertion

