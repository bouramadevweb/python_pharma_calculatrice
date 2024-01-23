import tkinter as tk

def create_button(master, text, row, col, command):
    tk.Button(master, text=text, command=command, width=5, height=2).grid(row=row, column=col, sticky="nsew")
def on_button_click(result_var, operator):
    current_text = result_var.get()

    if operator == '=':
        try:
            #  Mettre à jour le résultat
            result_var.set(str(eval(current_text)))
        except Exception as e:
            # Gérer les erreurs d'évaluation
            result_var.set("Erreur")
    elif operator == 'C':
        # Effacer le résultat actuel
        result_var.set("")
    else:
        # Ajouter l'opérateur au résultat actuel
        result_var.set(current_text + operator)


