import tkinter as tk


def calculer():
    weight = float(entrée_poids.get())
    bougie_format = format_choix.get()

    if bougie_format == "L":
        cire = 187
        stab = 11
        parf = 22
    else:
        cire = 296
        stab = 18.5
        parf = 37

    resultat_cire = weight * cire
    resultat_stabilisant = weight * stab
    resultat_parfum = weight * parf

    etiquette_resultat.configure(
        text=f"{resultat_cire} grammes de cire\n{resultat_stabilisant} grammes de stabilisant\n{resultat_parfum} grammes de parfum")


fenetre = tk.Tk()

label_poids = tk.Label(fenetre, text="Nombre de bougies :")
label_poids.pack()

entrée_poids = tk.Entry(fenetre)
entrée_poids.pack()

format_choix = tk.StringVar()
format_choix.set("L")

radio_bouton_L = tk.Radiobutton(
    fenetre, text="Format L", variable=format_choix, value="L")
radio_bouton_L.pack()

radio_bouton_M = tk.Radiobutton(
    fenetre, text="Format M", variable=format_choix, value="M")
radio_bouton_M.pack()

bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer)
bouton_calculer.pack()

etiquette_resultat = tk.Label(fenetre, text="")
etiquette_resultat.pack()

fenetre.mainloop()
