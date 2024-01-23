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
def run_calculator_app():
    root = tk.Tk()
    root.title("Calculatrice")

    result_var = tk.StringVar()
    result_entry = tk.Entry(root, textvariable=result_var, justify="right", font=("Arial", 14))
    result_entry.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Boutons pour les opérations de base
    create_button(root, '+', 1, 0, lambda: on_button_click(result_var, '+'))
    create_button(root, '-', 1, 1, lambda: on_button_click(result_var, '-'))
    create_button(root, '=', 1, 2, lambda: on_button_click(result_var, '='))

    for i in range(1, 3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    run_calculator_app()

