#Problem 32 from Euler Project
#Pandigital products



def euler_32():
    
    all_digit = set("123456789")
    product = set()
    acc = 0
    for a in range(1, 10000):
        for b in range(a, 10000):  # pour pas refaire les mêmes opérations
            if set(str(a * b) + str(a) + str(b)) == all_digit and len(str(a * b)) <= 4:
                product.add(a * b)
    print(product)
    return sum(list(product))


euler_32()