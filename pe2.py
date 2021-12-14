#Problem 2 from Euler Project
#Even Fibonacci numbers
#Completed on Mon, 15 Nov 2021, 05:34

first = 1
second = 2
actual = 0
sum = 2


while actual <= 4000000: 
    actual = first + second

    if actual % 2 == 0: 
        sum = sum + actual
    
    first = second
    second = actual
print(sum)