#Problem 40 from Euler Project
#Champernowne's constant
#Completed on Tue, 1 Mar 2022, 16:10
#Done in class


CHAMPERNOWNE_CONSTANT = 23456789101112131415161718192021


#
d = 0
#xpression = [1, 10, 100, 1000, 10000, 100000, 1000000]
for i in range(1, 7):
    d += 1 * 10 ** i
    
print(d)