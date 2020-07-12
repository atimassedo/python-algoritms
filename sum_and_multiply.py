def sum_and_multiply(ls):
    tmp = 1
    for i in ls:
        tmp *= i
    return sum(ls), tmp


r = sum_and_multiply([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10])
print(r)