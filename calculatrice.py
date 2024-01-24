"""import modul tkinter"""
import tkinter as tk # import tkinter
import csv # import csv
import math
class Calculatrice(tk.Tk):
    """class calculatrice """
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")

        self.resultat_var = tk.StringVar()
        self.resultat_var.set("0")

        # Entry
        entry_resultat = tk.Entry(self,
                                  textvariable=self.resultat_var,
                                  font=('Arial', 14), 
                                  justify='right',
                                  state='disabled')
        entry_resultat.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Fonction pour mettre à jour le résultat
        def mettre_a_jour_resultat(valeur):
            ancien_resultat = self.resultat_var.get()
            if ancien_resultat == "0" or ancien_resultat == "Erreur":
                self.resultat_var.set(valeur)
            else:
                self.resultat_var.set(ancien_resultat + valeur)

        # Fonction pour le résultat 
        def calculer_resultat():
            try:
                calcul = self.resultat_var.get()
                resul = eval(calcul)
                self.resultat_var.set(resul)          
            except ImportError as e:
                self.resultat_var.set(" error "+e)

        # Fonction pour enregistre dans  CSV
        def save_csv(calcul, result):
            try:
                with open('historique_calculs.csv', 'a', encoding="utf-8",newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([calcul, result])
            except ValueError as e:
                self.resultat_var.set("Erreur lors de l'enregistrement" +e)

        # Fonction pour annuler la dernière entrée
        def annuler():
            ancien_resultat = self.resultat_var.get()
            if ancien_resultat != "0" and ancien_resultat != "Erreur":
                self.resultat_var.set(ancien_resultat[:-1])

        # Fonction pour mémoriser dans le fichier CSV
        def memoriser_dans_csv():
            calcul = self.resultat_var.get()
            result = eval(calcul)
            save_csv(calcul, result)

        # Function for réinitialise la calculatrice
        def reset_calculatrice():
            self.resultat_var.set("0")

        # Function for clavier
        def write_clavier(event):
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

        # lire le clavier
        self.bind('<Key>', write_clavier)

        # Configuration des button
        bouton_memoriser = tk.Button(self, text='Memoriser',font=('Arial', 14),
                                     command=memoriser_dans_csv)
        bouton_memoriser.grid(row=5,column=0, sticky='nsew')

        bouton_annuler = tk.Button(self,text='Annuler',font=('Arial', 14),command=annuler)
        bouton_annuler.grid(row=5, column=1, sticky='nsew')

        bouton_reset = tk.Button(self, text='Reset', font=('Arial', 14), command=reset_calculatrice)
        bouton_reset.grid(row=5, column=2, sticky='nsew')

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
