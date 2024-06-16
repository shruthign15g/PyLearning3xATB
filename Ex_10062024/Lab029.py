# Logical Operators : and, or and not

def logical_operators(a, b):

    # and operator
    if a == 1 and b == 2:
        print("Both a and b are true")
    else:
        print("Either a or b is false, but not both")

    # or operator
    if a == 1 or b == 2:
        print("At least one of a or b is true")
    else:
        print("Neither a nor b is true")

    # not operator
    if not(a == 1 and b == 2):
        print("a and b are not both true")
    else:
        print("a and b are both true")