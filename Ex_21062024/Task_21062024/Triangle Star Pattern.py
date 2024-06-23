# programme to Traingle star pattern
#*
#**
#***
#****
#*****

def print_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
         print("*", end="")
        print()

print_triangle(5)

num = int(input(f"Enter the number of rows: "))
for i in range(num):
    for s in range(i+1):
        print("*", end=" ")
    print()



