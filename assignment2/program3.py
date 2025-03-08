def removevow(troll):
    return ''.join(word for word in troll if word not in ['a','e','i','o','u','A','E','I','O','U'])
print(removevow("This website is for losers LOL!"))
print("Ths wbst s fr lsrs LL!")