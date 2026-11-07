catalogue = {
    "P01": {"nom": "Ordinateur portable", "categorie": "Informatique", "prix": 45000},
    "P02": {"nom": "Imprimante", "categorie": "Informatique", "prix": 12000},
    "P03": {"nom": "Chaise de bureau", "categorie": "Mobilier", "prix": 6500},
    "P04": {"nom": "Ramette papier", "categorie": "Fournitures", "prix": 350}
}

# a) 
catalogue["P05"] = {
    "nom": "Bureau",
    "categorie": "Mobilier",
    "prix": 18000
}

# b) 
for produit in catalogue.values():
    if produit["categorie"] == "Informatique":
        produit["prix"] = round(produit["prix"] * 1.05)

# c) 
del catalogue["P04"]

# d) 
print("CODE      NOM                    CATEGORIE       PRIX")

for code, produit in catalogue.items():
    print(code, produit["nom"], produit["categorie"], produit["prix"])

# e) 
categories = {}

for produit in catalogue.values():
    cat = produit["categorie"]

    if cat not in categories:
        categories[cat] = []

    categories[cat].append(produit["prix"])

print("\nPrix moyen par catégorie :")

for cat, prix in categories.items():
    moyenne = sum(prix) / len(prix)
    print(cat, ":", moyenne)