import tkinter as tk
import csv
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

        # Fonction pour calculer le résultat et enregistrer dans un fichier CSV
        def calculer_resultat():
            try:
                calcul = self.resultat_var.get()
                resultat = eval(calcul)
                self.resultat_var.set(resultat)
            except Exception:
                self.resultat_var.set("Erreur")

        # Fonction pour enregistrer dans un fichier CSV
        def sauvegarder_csv(calcul, resultat):
            try:
                with open('historique_calculs.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([calcul, resultat])
            except Exception:
                self.resultat_var.set("Erreur lors de l'enregistrement")

        # Fonction pour annuler la dernière entrée
        def annuler():
            ancien_resultat = self.resultat_var.get()
            if ancien_resultat != "0" and ancien_resultat != "Erreur":
                self.resultat_var.set(ancien_resultat[:-1])

        # Fonction pour mémoriser dans le fichier CSV
        def memoriser_dans_csv():
            calcul = self.resultat_var.get()
            resultat = eval(calcul)
            sauvegarder_csv(calcul, resultat)

        # Fonction pour réinitialiser la calculatrice
        def reset_calculatrice():
            self.resultat_var.set("0")

        # Fonction pour gérer les saisies clavier
        def saisie_clavier(event):
            touche = event.char
            if touche.isdigit() or touche in ['+', '-', '*', '/', '.', '=']:
                mettre_a_jour_resultat(touche)
            elif touche == '\r':
                # La touche "Entrée" équivaut à "="
                calculer_resultat()

        # Configuration du poids des lignes et colonnes
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        # Lier la fonction saisie_clavier à l'événement de saisie clavier
        self.bind('<Key>', saisie_clavier)

        # Configuration des boutons spécifiques
        bouton_memoriser = tk.Button(self, text='Memoriser', font=('Arial', 14), command=memoriser_dans_csv)
        bouton_memoriser.grid(row=5, column=0, sticky='nsew')

        bouton_annuler = tk.Button(self, text='Annuler', font=('Arial', 14), command=annuler)
        bouton_annuler.grid(row=5, column=1, sticky='nsew')

        bouton_reset = tk.Button(self, text='Reset', font=('Arial', 14), command=reset_calculatrice)
        bouton_reset.grid(row=5, column=2, sticky='nsew')

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
