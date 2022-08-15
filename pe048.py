#Problem 9 from Euler Project
#Self powers
#Completed on Sat, 15 Jan 2022, 09:37
#Done in class



acc = 0
for i in range(1, 1001):
    acc += i ** i
print(acc % (10**10))
