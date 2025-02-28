f1 = open("test.jpeg", "rb+")
f2 = open("testoutput.jpeg", "wb+")

for i in f1:
    f2.write(i)