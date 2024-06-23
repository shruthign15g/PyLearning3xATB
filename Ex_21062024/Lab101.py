product_details = \
    {
        "product_1": {
            "name": "Laptop",
            "price": 1000,
            "quantity": 10
        },
        "product_2": {
            "name": "Mobile",
            "price": 500,
            "quantity": 20
        },

    }

print(product_details)
print(product_details["product_1"])
print(product_details.values())
print(product_details.keys())
print(product_details.items())

my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
print(my_dict)
print(len(my_dict))
print(my_dict['a'])
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
for i in my_dict: # using loop - dictionary
    print(i, my_dict[i])
my_list = list(my_dict)
print(list(my_dict.values()))
print(list(my_dict.keys()))
for i in list(my_dict.values()): # using loop - list
    print(i)

for j in list(my_dict.keys()):
        print(j)

for i, j in my_dict.items():
    print(i,j)




