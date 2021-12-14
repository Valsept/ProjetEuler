#Problem 4 from Euler Project
#Largest palindrome product
#Completed on Wed, 17 Nov 2021, 23:45


largest = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j

        
        if product > largest:
            s = str(i *j)
            if s == s[::-1]:
                largest = product

print ()