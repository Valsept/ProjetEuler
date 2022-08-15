#Problem 25 from Euler Project
#1000-digit Fibonacci number
#Completed on Tue, 8 Mar 2022, 10:05




a, b = (1, 1)
i = 2

while len(str(b)) < 1000:   
    a, b = (b, a + b)
    i += 1

print(i)
     










