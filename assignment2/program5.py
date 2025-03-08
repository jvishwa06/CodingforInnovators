def sortodd(arr):
    odd_numbers = sorted([x for x in arr if x % 2 != 0])
    # print(odd_numbers)

    odd_indx = 0
    result = []
    for num in arr:
        if num % 2 != 0:
            result.append(odd_numbers[odd_indx])
            # print(num,"if")
            odd_indx += 1
        else:
            result.append(num)
            # print(num, "else")
    return result
print(sortodd([9, 8, 4, 3]))