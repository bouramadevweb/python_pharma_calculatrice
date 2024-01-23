import tkinter as tk
from tkinter import ttk
import pandas as pd

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")

        self.resultat_var = tk.StringVar()
        self.resultat_var.set("0")

        # Entry pour afficher le résultat
        entry_resultat = tk.Entry(self, textvariable=self.resultat_var, font=('Arial', 14), justify='right', state='disabled')
        entry_resultat.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Fonction pour mettre à jour le résultat
        def mettre_a_jour_resultat(valeur):
            ancien_resultat = self.resultat_var.get()
            if ancien_resultat == "0" or ancien_resultat == "Erreur":
                self.resultat_var.set(valeur)
            else:
                self.resultat_var.set(ancien_resultat + valeur)

        # Fonction pour calculer le résultat
        def calculer_resultat():
            try:
                resultat = eval(self.resultat_var.get())
                self.resultat_var.set(resultat)
            except Exception:
                self.resultat_var.set("Erreur")

        # Fonction pour stocker dans un DataFrame Pandas et sauvegarder dans un fichier CSV
        def sauvegarder_csv():
            try: 
                resultat = eval(self.resultat_var.get())
                df = pd.DataFrame({'Calcul': [self.resultat_var.get()], 'Résultat': [resultat]})
                df.to_csv('historique_calculs.csv', mode='a', index=False, header=not df_exists())
            except Exception:
                self.resultat_var.set("Erreur")

        # Fonction pour vérifier si le fichier CSV existe
        def df_exists():
            try:
                pd.read_csv('historique_calculs.csv')
                return True
            except FileNotFoundError:
                return False

        # Fonction pour annuler la dernière entrée
        def annuler():
            ancien_resultat = self.resultat_var.get()
            if ancien_resultat != "0" and ancien_resultat != "Erreur":
                self.resultat_var.set(ancien_resultat[:-1])

        # Fonction pour gérer les saisies clavier
        def saisie_clavier(event):
            touche = event.char
            if touche.isdigit() or touche in ['+', '-', '*', '/', '.', '=']:
                mettre_a_jour_resultat(touche)
            elif touche == '\r':
                # La touche "Entrée" équivaut à "="
                calculer_resultat()

        # Configuration des boutons pour les opérateurs
        # operateurs = ['+', '-', '/', 'x']
        # operation_combobox = ttk.Combobox(self, values=operateurs)
        # operation_combobox.set('Choix')
        # operation_combobox.grid(row=5, column=2, sticky='nsew')

        # Configuration des boutons pour les opérations
        operations = [('=', 5, 2), ('Enregistrer', 5, 0), ('Annuler', 5, 1)]

        # Configuration des boutons pour les opérations
        for (texte, ligne, colonne) in operations:
            bouton = tk.Button(self, text=texte, font=('Arial', 14), command=lambda t=texte: calculer_resultat() if t == '=' else sauvegarder_csv() if t == 'Enregistrer' else annuler() if t == 'Annuler' else None)
            bouton.grid(row=ligne, column=colonne, sticky='nsew')

        # Lier la fonction saisie_clavier à l'événement de saisie clavier
        self.bind('<Key>', saisie_clavier)

        # Configuration du poids des lignes et colonnes
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
