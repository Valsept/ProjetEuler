##Problem 3 from Euler Project
#Largest prime factor
#Completed on Tue, 16 Nov 2021, 01:54

number = 600851475143
#i is the smallest prime number
i = 2
j = 0


while i*i <= number:
    while ( number % i == 0): 
        number = number/i
    i += 1

print(number)  