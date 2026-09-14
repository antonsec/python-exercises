letter = input("Enter your letter here: ").lower()

if letter in "aeiuo":
    print (f"{letter} is a vowel!")
elif letter in "y":
    print ("y is a vowel, and sometimes y is a consonant.")
else:
    print (f"{letter} is a consonant.")