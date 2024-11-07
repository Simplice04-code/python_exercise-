def remove_vowels(text):
    vowels = "AEIOUaeiou"  
    result = ""  

    
    for char in text:
    
        if char not in vowels:
            result += char
    return result


text = input("Enter a string of text: ")

print("Text without vowels:", remove_vowels(text))