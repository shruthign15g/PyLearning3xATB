# Tuple : collection of items in a specific order which is immutable

# Real scenario use case for tuples
#def tuple_operations():
#    """Performs common operations on tuples"""

# Creating a tuple with different data types
my_tuple = (1, 2.5, "Hello", [3, 4], (5, 6))

# Accessing elements in a tuple
print(my_tuple[2])  # Prints "Hello"

# Unpacking a tuple into variables
a, b, c, d, e = my_tuple
print(a, b,c,d,e)  # Prints 1, 2.5, "Hello", [3, 4], (5, 6)

# Slicing a tuple
print(my_tuple[2:4])  # Prints ("Hello", [3, 4])

# Modifying elements in a tuple doesn't work
# my_tuple[2] = "World"  # TypeError: 'tuple' object does not support item assignment

API_URLs = ("https://sdet.live/python0x", "https://awesomeqa.com","https://abc.com")
print(API_URLs)
print(API_URLs[0])