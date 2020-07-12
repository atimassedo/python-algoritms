def fill_array(n):
    i = [0] * n
    i[0], i[n-1] = 1, 1
    return i

print(fill_array(250))