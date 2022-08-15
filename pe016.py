#Problem 16 from Euler Project
#Power digit sum
#Completed on Thu, 13 Jan 2022, 00:03
#Done in class


acc = 0
for digit in str(2 ** 1000):
    acc += int(digit)
print(acc)
