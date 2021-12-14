#R#Problem 1 from Euler Project
#Multiples of 3 or 5
#Completed on Tue, 9 Nov 2021, 17:20

i = 0
multiples = 0
while i < 1000:
    if (i % 3 == 0 or i % 5 == 0):
        multiples += i
    i = i + 1


print(multiples)