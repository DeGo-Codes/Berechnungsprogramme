import tkinter as tk
from tkinter import messagebox

class SummenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Summenverwaltung")
        
        # Datenstruktur zur Speicherung
        self.zahlen_liste = []
        
        # UI Elemente
        self.eingabe = tk.Entry(root)
        self.eingabe.pack(pady=5)
        
        self.btn_add = tk.Button(root, text="Hinzufügen", command=self.hinzufuegen)
        self.btn_add.pack(pady=5)
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=5)
        
        self.btn_remove = tk.Button(root, text="Ausgewählte entfernen", command=self.entfernen)
        self.btn_remove.pack(pady=5)
        
        self.lbl_summe = tk.Label(root, text="Aktuelle Summe: 0", font=("Arial", 12, "bold"))
        self.lbl_summe.pack(pady=10)

    def aktualisiere_summe(self):
        aktuelle_summe = sum(self.zahlen_liste)
        self.lbl_summe.config(text=f"Aktuelle Summe: {aktuelle_summe}")

    def hinzufuegen(self):
        try:
            zahl = float(self.eingabe.get())
            self.zahlen_liste.append(zahl)
            self.listbox.insert(tk.END, zahl)
            self.eingabe.delete(0, tk.END)
            self.aktualisiere_summe()
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

    def entfernen(self):
        auswahl = self.listbox.curselection()
        if auswahl:
            index = auswahl[0]
            self.listbox.delete(index)
            self.zahlen_liste.pop(index)
            self.aktualisiere_summe()

if __name__ == "__main__":
    root = tk.Tk()
    app = SummenApp(root)
    root.mainloop()
