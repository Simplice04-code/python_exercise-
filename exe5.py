def list_to_dict(strings):
    return {string: len(string) for string in strings}
strings= ['apple','orange','avocado']
result= list_to_dict(strings)
print(result)