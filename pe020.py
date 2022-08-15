#Problem 20 from Euler Project
#Factorial digit sum
#Completed on Thu, 13 Jan 2022, 00:08
#Done in class



import math

acc = 0
for digit in str(math.factorial(100)):
    acc += int(digit)
print(acc)
