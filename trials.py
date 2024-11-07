camel_case = input("Enter your camel case here:")
for letter in camel_case:
    if letter.isupper():
        letter=letter.lower()
        print("_",end="")
    print(letter,end="")