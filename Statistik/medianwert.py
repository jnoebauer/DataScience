import tkinter as tk
from tkinter import messagebox
import statistics

# Funktion zur Berechnung des Medians und Mittelwerts
def berechne_median():
    eingabe = entry.get()
    try:
        # Umwandlung der Eingabe in eine Liste von Zahlen
        daten = [float(x.strip()) for x in eingabe.split(',') if x.strip()]
        if not daten:
            raise ValueError
        median = statistics.median(daten)
        mittelwert = statistics.mean(daten)
        messagebox.showinfo("Ergebnis", f"Der Median ist: {median}\nDer Mittelwert ist: {mittelwert}")
    except Exception:
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige, komma-getrennte Liste von Zahlen ein.")

# GUI erstellen
root = tk.Tk()
root.title("Median & Mittelwert berechnen")

label = tk.Label(root, text="Geben Sie eine Liste von Zahlen ein (durch Kommas getrennt):")
label.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

button = tk.Button(root, text="Median & Mittelwert berechnen", command=berechne_median)
button.pack(padx=10, pady=10)

root.mainloop()
