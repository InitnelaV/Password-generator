# Importation des modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

# Définition des variables
global password
global liste
global selection
maj = "ABCDEFGHJKMNPQRSTUVWXYZ"
min = "abcdefghjkmnpqrstuvwxyz"
chiffres = "0123456789"
charac_spec = "#*-+:@_&%!?"
liste = [maj, min, chiffres,charac_spec]
selection = [maj, min, chiffres,charac_spec]
random.shuffle(liste)

def combine(x):
    option = ((var_maj, 0), (var_min, 1), (var_num, 2), (var_spe, 3))
    if option[x][0].get() == True:
        liste.append(selection[option[x][1]])
    else:
        liste.remove(selection[option[x][1]])

def generate(event):
    "Génération de ton MDP"
    if liste == []:
        messagebox.showinfo(message="Selectionne au moins une option ;-)")
    else:
        try:
            nb = nbcar.get()
            if nb < 10 or nb > 30:
                messagebox.showinfo(message="La taille de ton pé...Heu, MDP doit faire entre minimum 10 caractères et maximum 30 caractères")
            else:
                compteur = 0
                position = -1
                D = []
                while compteur < nb:
                    if position < len(liste) - 1:
                        position += 1
                    else:
                        position = 0
                    D = D + random.sample(liste[position], 1)
                    compteur += 1
                random.shuffle(D)
                D = "".join(D)
                password.set(D)
        except:
            messagebox.showinfo(message="Indique un nombre de caractères pour le MDP et non autre chose patate! (smiley coeur)")


def addtoclip():
    text = password.get()
    if text == "":
        messagebox.showinfo(message="Génère ton MDP avant BG #Michou #TMTC ")
    else:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(text)


def windowcenter(w, h):
# Placer la fenêtre principal au centre de l'ecran"
    px = (fenetre.winfo_screenwidth() / 2) - (w / 2)
    py = (fenetre.winfo_screenheight() / 2) - (h / 2)
    fenetre.geometry("%dx%d+%d+%d" % (w, h, px, py))


# Création de l'interface graphique
fenetre = Tk()
fenetre.title("P@ssw0rd G€n€R@70r")
fenetre.config(bg="#f0f0f5")
fenetre.minsize(300, 200)
fenetre.resizable(width=False, height=False)

# Création des widgets checkbutton
var_maj = BooleanVar()
var_min = BooleanVar()
var_num = BooleanVar()
var_spe = BooleanVar()

var_maj.set(True)
var_min.set(True)
var_num.set(True)
var_spe.set(True)

chk_maj = ttk.Checkbutton(fenetre, text="Majuscules",
                          variable=var_maj, command=lambda: combine(0),
                          onvalue=True, offvalue=False)
chk_min = ttk.Checkbutton(fenetre, text="Minuscules",
                          variable=var_min, command=lambda: combine(1),
                          onvalue=True, offvalue=False)
chk_num = ttk.Checkbutton(fenetre, text="Chiffres",
                          variable=var_num, command=lambda: combine(2),
                          onvalue=True, offvalue=False)
chk_spe = ttk.Checkbutton(fenetre, text="Spéciaux",
                          variable=var_spe, command=lambda: combine(3),
                          onvalue=True, offvalue=False)

# Création des widgets label
label_nbcar = ttk.Label(text="Nombres de caractères souhaité")
label_pwd = ttk.Label(text="Your P@ssw0rd, mets toi sur la cellule et PRESS ENTER")

# Création des widgets entry
nbcar = IntVar()
nbcar.set('')
entree_nbcar = ttk.Entry(textvariable=nbcar)
password = StringVar()
entree_pwd = ttk.Entry(textvariable=password)


# Création du widget button
bouton_1 = ttk.Button(text="Copy / paste dans le presse papier", command=addtoclip)
bouton_2 = ttk.Button(text="Fermer l'outil du Turfu", command=quit)


# Placement des widgets
# Checkbutton
chk_maj.grid(column=1, row=1, sticky=W, padx=3, pady=3)
chk_min.grid(column=1, row=2, sticky=W, padx=3, pady=3)
chk_num.grid(column=2, row=1, sticky=W, padx=3, pady=3)
chk_spe.grid(column=2, row=2, sticky=W, padx=3, pady=3)

# Label et Entry pour nombre de caractères
label_nbcar.grid(column=1, row=3, columnspan=2, sticky='W', padx=3, pady=1)
entree_nbcar.grid(column=1, row=4, columnspan=2, sticky='WE', padx=3, pady=3)

# Label et Entry pour mot de passe
label_pwd.grid(column=1, row=5, columnspan=2, sticky='W', padx=3, pady=1)
entree_pwd.grid(column=1, row=6, columnspan=2, sticky='WE', padx=3, pady=3)

# Button pour copie du mot de passe dans le presse-papier
bouton_1.grid(column=1, row=7, columnspan=2, sticky='WE', padx=3, pady=3)

# Button pour fermer l'application
bouton_2.grid(column=1, row=8, columnspan=2, sticky='WE', padx=3, pady=3)

fenetre.bind('<Return>', generate)
fenetre.update_idletasks()
w = fenetre.winfo_reqwidth()
h = fenetre.winfo_reqheight()
windowcenter(w, h)

fenetre.mainloop()