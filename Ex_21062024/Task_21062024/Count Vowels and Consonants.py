#Write python code to count Vowels and Consonants in a string

def count_vowels_consonants(string):
    vowels = 0
    consonants = 0
    for char in string.lower():
        if char in 'aeiou':
            vowels += 1

        elif char.isalpha():
            consonants += 1

    print(vowels)
    print(consonants)
    return vowels, consonants

count_vowels_consonants("good morning")

# II Method
def vow_con_count(str):
    vow =0
    con =0
    for i in range(len(str)):
        ch = str[i]
        if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
                vow+=1

            else:
                con+=1
    print("Vowels: ",vow)
    print("Consonants: ", con)
    return (vow,con)

vow_con_count("hello world")





