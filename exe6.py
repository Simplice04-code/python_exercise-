def sentence_to_dict(sentence):
    sentence = sentence.lower()
    
    words = sentence.split()
    
    frequency_dict = {}

    for word in words:

        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict
sentence = input('Enter any sentence: ')
print (sentence_to_dict(sentence))