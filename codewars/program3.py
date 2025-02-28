def dig_pow(n):
    return ''.join([x for x in n if x!='!'])
print(dig_pow("hi!hi"))

def dig_pow(n, p):
    string = str(n)
    res = 0
    for i,char in enumerate(string):
        res += (int(char))**(i+p)
    print(res)
    k = res//n
    if (k*n) == res :
        return int(k)
    return -1
print(dig_pow(46288, 3))


def find_short(s):
    return min([len(x) for x in s.split()])
print(find_short("HOO HOW ARE YOU DA D arettt youtt"))


def func(milestohouse,milesforbunk, gallon):
    if milesforbunk <= (gallon * 25):
        print("Arjunaru villu....")
        if milestohouse > (gallon * 25):
            return print("Pondati waiting vro 🧨👠put petrol and go fast")
    else:
        return print("It's very wrong bro!! put petrol")
print(func(50,40,2))


def solution(text, ending):
    length = len(ending)
    # print(text[-length:])
    if text[-length:] == ending:
        return print("True")
    return print("False")
solution('abc','bc')


def digital_root(n):
    if n < 10:
        return n
    string_num = str(n)
    res = 0
    while len(string_num) > 1:
        res = sum(int(char) for char in string_num)
        string_num = str(res)
    return res
print(digital_root(493193))
print(digital_root(9))


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))




def create_phone_number(n):
    lis = ''.join(map(str, n))
    print(lis)
    print(f"({lis[0:3]}) {lis[3:6]}-{lis[6:]}")

create_phone_number([0,1,3,4,5,6,7,8,9])