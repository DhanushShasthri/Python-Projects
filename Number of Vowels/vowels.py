def count_vowel(string):
    vowel=0
    set={'a','e','i','o','u'}
    for i in string.lower():
        if i in set:
            vowel+=1
    return vowel
print("Enter the string")
string=input()
vowel=count_vowel(string)
print(f"The entered stinrg {string} contains {vowel} vowels")
