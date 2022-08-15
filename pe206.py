#Problem 206 from Euler Project
#Concealed Square
#Completed on Mon, 15 Aug 2022, 15:14
#Done in class


def euler_206():
    for n in range(1389026620, 1010101010, -10):
        if str(n * n)[::2] == "1234567890":

            return n


euler_206()