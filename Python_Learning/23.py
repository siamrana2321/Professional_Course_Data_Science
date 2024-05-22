################ 23. Check if an alphabet is vowel or consonant ################
char = input("Enter an alphabet: ")
vowels = ['a', 'e', 'i', 'o', 'u']

if char.lower() in vowels:
    print("Vowel")
else:
    print("Consonant")