#Problem 9 from Euler Project
#Special Pythagorean triplet
#Completed on Tue, 8 Feb 2022, 12:07
#Done in class



ef is_pythagorean(a, b, c):
    return a*a + b*b == c*c


def pythagorean_triplet_product(n):
    for a in range(1, n):
        for b in range(1, n):
            c = n - a - b
            if a < b < c and is_pythagorean(a, b, c):
                return a * b *c

pythagorean_triplet_product(1000)