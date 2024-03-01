def trier():
    nombres = []
    while True:
        entree = input("Entrez un nombre ou 'stop' pour terminer la saisie : ")
        if entree == 'stop':
            break
        elif entree.isdigit():
            nombres.append(int(entree))
        else:
            print("Veuillez entrer un nombre entier valide ou 'stop' pour terminer.")

    nombres_bons = sorted(nombres)
    return nombres_bons

suite_bons = trier()
print("Suite triée :", suite_bons)