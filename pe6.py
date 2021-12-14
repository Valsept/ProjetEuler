#Problem 6 from Euler Project
#Sum square difference
#Completed on Thu, 18 Nov 2021, 12:55

sum = 0
sum_square = 0

for i in range(1, 101, 1):
    sum_square += i**2
    sum += i

sum = sum **2

print(sum - sum_square)