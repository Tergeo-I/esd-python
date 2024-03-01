import tkinter as tk
from tkinter import messagebox

def trier():
    entree = entree_entry.get()
    nombres = []
    for nombre in entree.split(','):
        nombre = nombre.strip()  # Supprimer les espaces avant et après le nombre
        if nombre == 'stop':
            break
        elif nombre.isdigit():
            nombres.append(int(nombre))
        else:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres entiers séparés par des virgules ou 'stop' pour terminer.")
            return
    
    nombres_bons = sorted(nombres)
    suite_label.config(text="Suite triée : " + ", ".join(map(str, nombres_bons)))

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface de tri de nombres")

# Créer les widgets
entree_label = tk.Label(root, text="Entrez des nombres séparés par des virgules ou 'stop' pour terminer la saisie :")
entree_label.pack()

entree_entry = tk.Entry(root)
entree_entry.pack()

trier_button = tk.Button(root, text="Trier", command=trier)
trier_button.pack()

suite_label = tk.Label(root, text="Suite triée :")
suite_label.pack()

# Lancer la boucle principale
root.mainloop()
