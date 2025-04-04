import tkinter as tk
class Drzave:
    def __init__(self,ime_drzave,glavni_grad,broj_stanovnika):
        self.ime_drzave=ime_drzave
        self.glavni_grad=glavni_grad
        self.broj_stanovnika = int(broj_stanovnika)

    def __str__(self):
        return f"{self.ime_drzave}|{self.glavni_grad}|{self.broj_stanovnika}"

class Countries:
    def __init__(self):
        self.lista_drzava = []
        self.ucitavanje_fajla("drzave.txt")

    def ucitavanje_fajla(self,naziv):
        linija = [line.strip() for line in open(naziv)]
        for i in linija:
            informacije = i.split("|")
            self.lista_drzava.append(Drzave(informacije[0], informacije[1], informacije[2]))

    def drzava_sa_najvise_stanovnika(self):
        drzava_sa_najvise = self.lista_drzava[0]
        for i in self.lista_drzava:
            if i.broj_stanovnika > drzava_sa_najvise.broj_stanovnika:
                drzava_sa_najvise = i
        return drzava_sa_najvise

    def drzava_sa_najmanje_stanovnika(self):
        drzava_sa_min_stanovnika = self.lista_drzava[0]
        for i in self.lista_drzava:
            if i.broj_stanovnika < drzava_sa_min_stanovnika.broj_stanovnika:
                drzava_sa_min_stanovnika = i
        return drzava_sa_min_stanovnika

    def drzava_po_glavnom_gradu(self,glavni_grad):
        for i in self.lista_drzava:
            if i.glavni_grad.lower() == glavni_grad.lower():
                return i.ime_drzave

    def drzave_u_opsegu(self, min_stanovnika, max_stanovnika):
        drzave_u_opsegu = []
        for i in self.lista_drzava:
            if min_stanovnika <= i.broj_stanovnika <= max_stanovnika:
                drzave_u_opsegu.append(i)
        return drzave_u_opsegu

    def ispis_u_fajl(self, naziv_fajla):
        with open(naziv_fajla, "a") as fajl:
            for i in self.lista_drzava:
                fajl.write(f"{i.ime_drzave}|{i.glavni_grad}|{i.broj_stanovnika}\n")


#GUI

root = tk.Tk()
root.title("Države")

countries = Countries()

listbox = tk.Listbox(root, height=10, width=50)
listbox.grid(row=0, column=0, columnspan=3)

def prikazi_sve():
    listbox.delete(0, tk.END)
    for i in countries.lista_drzava:
        listbox.insert(tk.END, i)

def pretrazi_po_gradu():
    grad=unos_grada.get().strip()
    if grad:
        drzava=countries.drzava_po_glavnom_gradu(grad)

        top=tk.Toplevel()
        top.title("Rezultat pretrage")

        if drzava:
            result_label = tk.Label(top, text=f"Država sa gradom {grad} je: {drzava}")
            result_label.pack(padx=20, pady=20)
        else:
            result_label = tk.Label(top, text="Nema države sa tim gradom.")
            result_label.pack(padx=20, pady=20)

def pretrazi_po_broju_stanovnika():
    min_stanovnika_value=unos_min_stanovnika.get()
    max_stanovnika_value=unos_max_stanovnika.get()

    if min_stanovnika_value.isdigit() and max_stanovnika_value.isdigit():
        min_stanovnika_value=int(min_stanovnika_value)
        max_stanovnika_value=int(max_stanovnika_value)
        drzave=countries.drzave_u_opsegu(min_stanovnika_value, max_stanovnika_value)
        top = tk.Toplevel()
        top.title("Rezultat pretrage")

        if drzave:
            for i in drzave:
                result_label = tk.Label(top, text=str(i))
                result_label.pack(padx=20, pady=10)
        else:
            result_label = tk.Label(top, text="Nema država u tom opsegu.")
            result_label.pack(padx=20, pady=20)
    else:
        label_rezultat.config(text="Unesite validan broj stanovnika.")

def prikazi_najvise_stanovnika():
    drzava=countries.drzava_sa_najvise_stanovnika()
    top=tk.Toplevel()
    top.title("Rezultat pretrage")
    result_label=tk.Label(top, text=f"Država sa najviše stanovnika: {drzava.ime_drzave}")
    result_label.pack(padx=20, pady=20)

def prikazi_najmanje_stanovnika():
    drzava = countries.drzava_sa_najmanje_stanovnika()
    top = tk.Toplevel()
    top.title("Rezultat pretrage")
    result_label = tk.Label(top, text=f"Država sa najmanje stanovnika: {drzava.ime_drzave}")
    result_label.pack(padx=20, pady=20)

def sacuvaj_u_fajl():
    countries.ispis_u_fajl("ispis_drzava.txt")
    label_rezultat.config(text="Podaci su sačuvani u fajl.")

tk.Button(root, text="Prikaži sve države", command=prikazi_sve).grid(row=1, column=0)

unos_grada = tk.Entry(root)
unos_grada.grid(row=1, column=1)
tk.Button(root, text="Pretraži po glavnom gradu", command=pretrazi_po_gradu).grid(row=1, column=2)

unos_min_stanovnika = tk.Entry(root)
unos_min_stanovnika.grid(row=2, column=0)
unos_max_stanovnika = tk.Entry(root)
unos_max_stanovnika.grid(row=2, column=1)
tk.Button(root, text="Pretraži po broju stanovnika", command=pretrazi_po_broju_stanovnika).grid(row=2, column=2)

tk.Button(root, text="Najveći broj stanovnika", command=prikazi_najvise_stanovnika).grid(row=3, column=0)
tk.Button(root, text="Najmanji broj stanovnika", command=prikazi_najmanje_stanovnika).grid(row=3, column=1)

label_rezultat = tk.Label(root, text="")
label_rezultat.grid(row=4, column=0, columnspan=3)

tk.Button(root, text="Sačuvaj u fajl", command=sacuvaj_u_fajl).grid(row=5, column=0, columnspan=3)

root.mainloop()