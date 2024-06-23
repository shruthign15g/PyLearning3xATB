# Write a python code to reverse string

def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    print(str)
    return str

s = ("Welcome to Testing Academy")
reverse_string("Welcome to Testing Academy")
print("The original string is :", end = "")
print("The reversed string is :", reverse_string(s))
#print(reverse_string(s))




