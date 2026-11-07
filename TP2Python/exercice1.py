jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]

# a) total et moyenne
total = sum(ventes)
moyenne = total / len(ventes)
print("Total :", total)          
print("Moyenne :", moyenne)     

# b) meilleur jour
meilleur = jours[ventes.index(max(ventes))]
print("Meilleur jour :", meilleur)   # Vendredi

