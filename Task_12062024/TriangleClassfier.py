# Write programme to classify a triangle based on length of its sides

def classify_triangle(a, b, c):
    """
    Classify a triangle based on the lengths of its sides.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.

    Returns:
        str: The type of triangle identified based on the side lengths.
    """

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the sides form a valid triangle
    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid Triangle"

    # Classify the triangle based on side lengths
    if a == b and b == c:
        return "Equilateral Triangle"
    elif a != b and b != c and a != c:
        return "Scalene Triangle"
    else:
        return "Isosceles Triangle"

triangle_type = classify_triangle(a, b, c)
print(triangle_type)