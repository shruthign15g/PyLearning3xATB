# Write a code to check if two given strings are anagrams of each other.
def are_anagrams(str1, str2):

    if len(str1) != len(str2): # Check if the lengths are different
        return False

    char_count = {} # Create a dictionary to store character counts

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1 # Count characters in the first string

    for char in str2: # Decrement character counts for the second string
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count) == 0  # If the dictionary is empty, all characters were matched


print(are_anagrams("test", "sett"))# True
