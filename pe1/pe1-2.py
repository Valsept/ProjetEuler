#pe1 without any loop, done in class

def arithmetic_series(start, stop, step):
    un_1 = stop - step
    n = (stop - start) // step
    return n * (start + un_1) // 2
    
i = arithmetic_series(3, 1002, 3)
j = arithmetic_series(5, 1005, 5)
k = arithmetic_series(15, 1005, 15)

print(i + j - k)
