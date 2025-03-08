def sum_of_multiples(num):
    if num<0:
        return 0
    summ =  0
    for i in range(num):
        if i%3 == 0 or i%5==0:
            summ+=i
    return summ
print(sum_of_multiples(10))
print(3+5+6+9)