# Dictionary :  Key and Value pairs, Unordered, Mutable
# Creating a dictionary
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# or
# mydict = dict(name="Max", age=28, city="New York")

my_dict1 = {
    "name" : "Ankit",
    "age" : 24,
    "city" : "New york"
}
print(my_dict1)
print(my_dict1["name"])
print(my_dict1["age"])
print(my_dict1["city"])
print(my_dict1.get("name"))
print(len(my_dict1))
print(my_dict1.keys())
print(my_dict1.values())

phone_book = dict(name = "John", age = 28, gender = 'M')


print(phone_book)