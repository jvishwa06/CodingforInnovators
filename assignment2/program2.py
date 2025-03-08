import re
def toCamelCase(s):
    words = re.split('[-_]', s)
    # print(words)
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(toCamelCase("the-stealth-warrior"))  
print(toCamelCase("The_Stealth_Warrior"))  
print(toCamelCase("The_Stealth-Warrior"))  