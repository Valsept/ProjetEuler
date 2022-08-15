#Problem 9 from Euler Project
#Self powers
#Completed on Sat, 15 Jan 2022, 09:37
#Done in class


def digital_sum(number):
    acc = 0
    for digit in str(number):
        acc += int(digit)
    return acc


result = 0
for a in range(1, 100):
    for b in range(1, 100):
        result = max(result, digital_sum(a ** b))
print(result)
