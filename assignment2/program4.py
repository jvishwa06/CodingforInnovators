def sortbynum(s):
    words = s.split()  

    def extract_num_func(word):
        return int(''.join([char for char in word if char.isdigit()]))

    words.sort(key=extract_num_func)    
    return ' '.join(words)  

print(sortbynum("is2 Thi1s T4est 3a"))