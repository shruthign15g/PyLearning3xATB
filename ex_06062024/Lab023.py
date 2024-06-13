# List - Shopping List - it is list of items
# Milk, Bread, Butter, Eggs, Cookies
# 1. Add item, Remove item, Update item, View item, Exit

shopping_list =  ["Milk","Bread","Butter","Eggs","Cookies"]
print(shopping_list)
print(len(shopping_list))
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("Chocolate") # add item to list
print(shopping_list)
shopping_list.insert(1,"Sugar") # add item to list in middle
print(shopping_list)
shopping_list.remove("Butter") # remove item from list
print(shopping_list)
shopping_list.extend(["Chips","Coffee"]) # add multiple items to list
print(shopping_list.pop())
print(shopping_list.index("Eggs"))
shopping_list.reverse()
print(shopping_list)
shopping_list[0] = "Honey"
print(shopping_list)
shopping_list.sort()
print(shopping_list)

My_list = [1,"John", 2.13]
print(My_list)