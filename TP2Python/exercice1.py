jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]

# a)
total = sum(ventes)
moyenne = total / len(ventes)
print("Total :", total)
print("Moyenne :", moyenne)

# b)
maximum = max(ventes)
position = ventes.index(maximum)
print("Meilleur jour :", jours[position])

# c)
print("Jours au-dessus de la moyenne :")
for i in range(len(ventes)):
    if ventes[i] > moyenne:
        print(jours[i], ventes[i])

# d)
print("Classement :")
ventes_triees = sorted(ventes, reverse=True)
for v in ventes_triees:
    position = ventes.index(v)
    print(jours[position], v)