#Problem 7 from Euler Project
#10001st prime
#Completed on Tue, 14 Dec 2021, 12:14

def is_prime (nomber):
    if nomber == 1:
        return False
    if nomber%2 == 0:
        return False
    for i in range(3, int(nomber**0.5)+1, 2):
        if nomber%i == 0:
            return False
    return True

number = 1
position = 1

while position != 10001:
    number += 2
    if is_prime(number):
        position += 1
print(number)

#Check if it divide by 2 / 3 / 5 
