x, y, z = (15, 35, 40)
print(x)

t = (15, 35, 40)
print(t)

# t.append() # tuple are immutable in nature

new_t = t + (4,)
print(new_t) # Alternative way to add the element to tuple

my_list = list(t)
print(my_list)
my_list.append(55)
new_t2 = tuple(my_list)
print(new_t2)
