#Problem 17 from Euler Project
#Power digit sum
#Completed on Thu, 13 Jan 2022, 00:03
#Done in class

from num2words import num2words

result = 0
for i in range(1, 1001):
    for symbol in num2words(i):
        if "a" <= symbol <= "z":
            result += 1
print(result)