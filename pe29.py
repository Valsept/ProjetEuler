#Problem 29 from Euler Project
#Distinct powers
#Completed on Tue, 15 Mar 2022, 15:20



#my_set.add(5) # ajouter l'entier 5 comme élément de my_set (si besoin)
#my_set.remove(5) # le supprimer

list = set()
for a in range(2,101):
    for b in range(2,101):
        list.add(a**b)
len(list)