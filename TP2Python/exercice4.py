ventes = [("Aicha", 12000), ("Sidi", 8000), ("Aicha", 15500),
          ("Mohamed", 4000), ("Sidi", 22000), ("Aicha", 3000),
          ("Fatimetou", 18000)]

# a) 
vendeurs = {nom for nom, montant in ventes}
print(len(vendeurs))        

# b) nombre de ventes et chiffre d'affaires
nb = {}
ca = {}
for nom, montant in ventes:
    nb[nom] = nb.get(nom, 0) + 1
    ca[nom] = ca.get(nom, 0) + montant
print(nb)   
print(ca)  
# c) 
for nom in sorted(ca, key=ca.get, reverse=True):
    print(nom, ca[nom])
