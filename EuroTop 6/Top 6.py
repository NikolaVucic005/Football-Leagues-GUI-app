from tkinter import *
from tkinter import messagebox

def Engleska():
    top=Toplevel()
    top.geometry("500x510")
    top.title("Engleska liga")
    engleska_labela=Label(top,text="Klubovi u Premijer ligi")
    engleski_listbox=Listbox(top)
    with open("premijer_liga.txt")as file:
        for i in file:
            engleski_listbox.insert(END,i)

    engleska_labela2=Label(top,text="Klubovi u Championship-u")
    engleski_listbox2=Listbox(top)
    with open("championship.txt")as file:
        for i in file:
            engleski_listbox2.insert(END,i)

    engleska_labela3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    engleski_entry=Entry(top)
    engleski_listbox3=Listbox(top)

    def Trofeji_klubova_premijerliga():
        top1=Toplevel()
        top1.title("Trofeji Premijerliga")
        top1.geometry("300x300")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova Premijer lige")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_premijerliga.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_listbox.config(height=15,width=25)
        trofeji_labela.pack()
        trofeji_listbox.pack()

    def Trofeji_klubova_championship():
        top2=Toplevel()
        top2.title("Trofeji Championship")
        top2.geometry("300x300")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klubova Championship-a")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_championship.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15, width=25)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if engleski_entry.get()=="Premijer liga" or engleski_entry.get()=="premijer liga":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Premijer liga")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_premijerliga.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if engleski_entry.get().isdigit()==True:
                raise ValueError

            if engleski_entry.get()=="":
                raise ValueError

            if engleski_entry.get()!="Premijer liga" and engleski_entry.get()!="premijer liga" and engleski_entry.get()!="Championship" and engleski_entry.get()!="championship":

                raise ValueError

            if engleski_entry.get().isnumeric() == True:
                raise ValueError

            if engleski_entry.get() == "Championship" or engleski_entry.get() == "championship":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Championship")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_championship.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3=Toplevel()
        top3.title("Online Prodavnica Engleska")
        top3.geometry("400x435")
        prodavnica_labela=Label(top3,text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox=Listbox(top3)
        prodavnica_listbox2=Listbox(top3)
        with open("prodavnica_engleska.txt")as file:
            for i in file:
                prodavnica_listbox.insert(END,i)

        def Korpa():
            try:
                dobijanje=prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END,dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje","Morate da izaberete artikal da bi ste ga dodali u korpu!")


        def Kupi_artikle_iz_korpe():
            try:
                kupovina=len(prodavnica_listbox2.get(0,END))
                if kupovina==0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena",f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje","U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje=prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska","Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme=Button(top3,text="Ukloni artikal iz korpe",command=Ukloni_artikal_iz_korpe)

        def Karte_premijerliga():
            top4=Toplevel()
            top4.title("Karte za utakmice Premijer lige")
            top4.geometry("300x120")
            karte_labela=Label(top4,text="Izaberite kartu koju zelite da kupite")
            karte_listbox=Listbox(top4)
            with open("karte_premijerliga.txt")as file:
                for i in file:
                    karte_listbox.insert(END,i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4,width=35)

            def Kupovina_karte_premijerliga():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_premijerliga)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_championship():
            top5=Toplevel()
            top5.title("Karte za utakmice Championship-a")
            top5.geometry("300x120")
            karte_championship_labela=Label(top5,text="Izaberite kartu koju zelite da kupite")
            karte_championship_listbox=Listbox(top5)
            with open("karte_championship.txt")as file:
                for i in file:
                    karte_championship_listbox.insert(END,i)

            karte_championship_labela.pack()
            karte_championship_listbox.pack()
            karte_championship_listbox.config(height=4,width=35)

            def Kupovina_karte_championship():
                try:
                    dobijena_karta=karte_championship_listbox.get(karte_championship_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_championship)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        prodavnica_dugme = Button(top3,text="Dodaj u korpu",command=Korpa)
        prodavnica_dugme2=Button(top3,text="Kupovina karata za utakmice Premijer lige",command=Karte_premijerliga)
        prodavnica_dugme3=Button(top3,text="Kupovina karata za utakmice Championship-a",command=Karte_championship)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        prodavnica_dugme.pack()
        korpa_labela.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    englesko_dugme3=Button(top,text="Prikaz trofeja za klubove Premijer lige",command=Trofeji_klubova_premijerliga)
    englesko_dugme4=Button(top,text="Prikaz trofeja za klubove Championship-a",command=Trofeji_klubova_championship)
    englesko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    englesko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    engleski_listbox.config(width=25)
    engleski_listbox2.config(width=25)

    engleska_labela.pack()
    engleski_listbox.pack()
    englesko_dugme3.pack()
    engleska_labela2.pack()
    engleski_listbox2.pack()
    englesko_dugme4.pack()
    engleska_labela3.pack()
    engleski_entry.pack()
    englesko_dugme6.pack()
    englesko_dugme5.pack()

def Spanija():
    top=Toplevel()
    top.geometry("500x510")
    top.title("Spanska liga")
    spanska_labela=Label(top,text="Klubovi u La ligi")
    spanski_listbox=Listbox(top)
    with open("laliga.txt")as file:
        for i in file:
            spanski_listbox.insert(END,i)

    spanska_labela2=Label(top,text="Klubovi u Segunda ligi")
    spanski_listbox2=Listbox(top)
    with open("segunda.txt")as file:
        for i in file:
            spanski_listbox2.insert(END,i)

    spanska_labela3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    spanski_entry=Entry(top)

    def Trofeji_klubova_laliga():
        top1=Toplevel()
        top1.title("Trofeji La liga")
        top1.geometry("300x300")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova La lige")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_laliga.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_listbox.config(height=15,width=25)
        trofeji_labela.pack()
        trofeji_listbox.pack()

    def Trofeji_klubova_segunda():
        top2=Toplevel()
        top2.title("Trofeji Segunda lige")
        top2.geometry("300x300")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klubova Segunda lige")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_segunda.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15,width=26)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if spanski_entry.get()=="La liga" or spanski_entry.get()=="la liga":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica La liga")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_laliga.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if spanski_entry.get().isdigit()==True:
                raise ValueError

            if spanski_entry.get()=="":
                raise ValueError

            if spanski_entry.get()!="La liga" and spanski_entry.get()!="la liga" and spanski_entry.get()!="Segunda liga" and spanski_entry.get()!="segunda liga":
                raise ValueError

            if spanski_entry.get().isnumeric()==True:
                raise ValueError

            if spanski_entry.get() == "Segunda liga" or spanski_entry.get() == "segunda liga":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Segunda liga")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_segunda.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3 = Toplevel()
        top3.title("Online Prodavnica Spanija")
        top3.geometry("400x435")
        prodavnica_labela = Label(top3, text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox = Listbox(top3)
        prodavnica_listbox2 = Listbox(top3)
        with open("prodavnica_spanija.txt") as file:
            for i in file:
                prodavnica_listbox.insert(END, i)

        def Korpa():
            try:
                dobijanje = prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END, dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate da izaberete artikal da bi ste ga dodali u korpu!")

        def Kupi_artikle_iz_korpe():
            try:
                kupovina = len(prodavnica_listbox2.get(0, END))
                if kupovina == 0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena", f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje",
                                        "U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje = prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska", "Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme = Button(top3, text="Ukloni artikal iz korpe", command=Ukloni_artikal_iz_korpe)

        def Karte_laliga():
            top4 = Toplevel()
            top4.title("Karte za utakmice La lige")
            top4.geometry("300x120")
            karte_labela = Label(top4, text="Izaberite kartu koju zelite da kupite")
            karte_listbox = Listbox(top4)
            with open("karte_laliga.txt") as file:
                for i in file:
                    karte_listbox.insert(END, i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4, width=35)

            def Kupovina_karte_laliga():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_laliga)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_segundaliga():
            top5 = Toplevel()
            top5.title("Karte za utakmice Segunda lige")
            top5.geometry("300x120")
            karte_segunda_labela = Label(top5, text="Izaberite kartu koju zelite da kupite")
            karte_segunda_listbox = Listbox(top5)
            with open("karte_segunda.txt") as file:
                for i in file:
                    karte_segunda_listbox.insert(END, i)

            karte_segunda_labela.pack()
            karte_segunda_listbox.pack()
            karte_segunda_listbox.config(height=4, width=35)

            def Kupovina_karte_segundaliga():
                try:
                    dobijena_karta=karte_segunda_listbox.get(karte_segunda_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_segundaliga)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        prodavnica_dugme = Button(top3, text="Dodaj u korpu", command=Korpa)
        prodavnica_dugme2 = Button(top3, text="Kupovina karata za utakmice La lige", command=Karte_laliga)
        prodavnica_dugme3 = Button(top3, text="Kupovina karata za utakmice Segunda lige", command=Karte_segundaliga)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        korpa_labela.pack()
        prodavnica_dugme.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    spansko_dugme3=Button(top,text="Prikaz trofeja za klubove La lige",command=Trofeji_klubova_laliga)
    spansko_dugme4=Button(top,text="Prikaz trofeja za klubove Segunda lige",command=Trofeji_klubova_segunda)
    spansko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    spansko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    spanski_listbox.config(width=25)
    spanski_listbox2.config(width=25)
    spanska_labela.pack()
    spanski_listbox.pack()
    spansko_dugme3.pack()
    spanska_labela2.pack()
    spanski_listbox2.pack()
    spansko_dugme4.pack()
    spanska_labela3.pack()
    spanski_entry.pack()
    spansko_dugme6.pack()
    spansko_dugme5.pack()

def Italija():
    top=Toplevel()
    top.title("Italijanska liga")
    top.geometry("500x510")
    italijanska_labela=Label(top,text="Klubovi u Seriji A")
    italijanski_listbox=Listbox(top)
    with open("serijaa.txt")as file:
        for i in file:
            italijanski_listbox.insert(END,i)

    italijanska_labela2=Label(top,text="Klubovi u Seriji B")
    italijanski_listbox2=Listbox(top)
    with open("serijab.txt")as file:
        for i in file:
            italijanski_listbox2.insert(END,i)

    italijanska_labela3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    italijanski_entry=Entry(top)

    def Trofeji_klubova_serijaa():
        top1=Toplevel()
        top1.title("Trofeji Serija A")
        top1.geometry("300x300")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova Serije A")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_serijaa.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_listbox.config(height=15,width=25)
        trofeji_labela.pack()
        trofeji_listbox.pack()

    def Trofeji_klubova_serijab():
        top2=Toplevel()
        top2.title("Trofeji Serija B")
        top2.geometry("300x300")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klubova Serije B")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_serijab.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15,width=25)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if italijanski_entry.get()=="Serija A" or italijanski_entry.get()=="serija a":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Serija A")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_serijaa.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if italijanski_entry.get().isdigit()==True:
                raise ValueError

            if italijanski_entry.get()=="":
                raise ValueError

            if italijanski_entry.get()!="Serija A" and italijanski_entry.get()!="serija a" and italijanski_entry.get()!="Serija B" and italijanski_entry.get()!="serija b":
                raise ValueError

            if italijanski_entry.get().isnumeric()==True:
                raise ValueError

            if italijanski_entry.get() == "Serija B" or italijanski_entry.get() == "serija b":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Serija B")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_serijab.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3 = Toplevel()
        top3.title("Online Prodavnica Italija")
        top3.geometry("400x435")
        prodavnica_labela = Label(top3, text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox = Listbox(top3)
        prodavnica_listbox2 = Listbox(top3)
        with open("prodavnica_italija.txt") as file:
            for i in file:
                prodavnica_listbox.insert(END, i)

        def Korpa():
            try:
                dobijanje = prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END, dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate da izaberete artikal da bi ste ga dodali u korpu!")

        def Kupi_artikle_iz_korpe():
            try:
                kupovina = len(prodavnica_listbox2.get(0, END))
                if kupovina == 0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena", f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje",
                                        "U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje = prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska", "Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme = Button(top3, text="Ukloni artikal iz korpe", command=Ukloni_artikal_iz_korpe)

        def Karte_serijaa():
            top4 = Toplevel()
            top4.title("Karte za utakmice Serija A")
            top4.geometry("300x120")
            karte_labela = Label(top4, text="Izaberite kartu koju zelite da kupite")
            karte_listbox = Listbox(top4)
            with open("karte_serijaa.txt") as file:
                for i in file:
                    karte_listbox.insert(END, i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4, width=35)

            def Kupovina_karte_serijaa():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_serijaa)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_serijab():
            top5 = Toplevel()
            top5.title("Karte za utakmice Serija B")
            top5.geometry("300x120")
            karte_serijab_labela = Label(top5, text="Izaberite kartu koju zelite da kupite")
            karte_serijab_listbox = Listbox(top5)
            with open("karte_serijab.txt") as file:
                for i in file:
                    karte_serijab_listbox.insert(END, i)

            karte_serijab_labela.pack()
            karte_serijab_listbox.pack()
            karte_serijab_listbox.config(height=4, width=35)

            def Kupovina_karte_serijab():
                try:
                    dobijena_karta=karte_serijab_listbox.get(karte_serijab_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_serijab)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        prodavnica_dugme = Button(top3,text="Dodaj u korpu",command=Korpa)

        prodavnica_dugme = Button(top3, text="Dodaj u korpu", command=Korpa)
        prodavnica_dugme2 = Button(top3, text="Kupovina karata za utakmice Serija A", command=Karte_serijaa)
        prodavnica_dugme3 = Button(top3, text="Kupovina karata za utakmice Serija B", command=Karte_serijab)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        prodavnica_dugme.pack()
        korpa_labela.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    italijansko_dugme3=Button(top,text="Prikaz trofeja za klubove Serije A",command=Trofeji_klubova_serijaa)
    italijansko_dugme4=Button(top,text="Prikaz trofeja za klubove Serije B",command=Trofeji_klubova_serijab)
    italijansko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    italijansko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    italijanski_listbox.config(width=25)
    italijanski_listbox2.config(width=25)
    italijanska_labela.pack()
    italijanski_listbox.pack()
    italijansko_dugme3.pack()
    italijanska_labela2.pack()
    italijanski_listbox2.pack()
    italijansko_dugme4.pack()
    italijanska_labela3.pack()
    italijanski_entry.pack()
    italijansko_dugme6.pack()
    italijansko_dugme5.pack()

def Nemacka():
    top=Toplevel()
    top.title("Nemacka liga")
    top.geometry("500x510")
    nemacka_labela=Label(top,text="Klubovi u Bundes ligi")
    nemacki_listbox=Listbox(top)
    with open("bundesliga.txt")as file:
        for i in file:
            nemacki_listbox.insert(END,i)

    nemacka_labela2=Label(top,text="Klubovi u Bundes ligi 2")
    nemacki_listbox2=Listbox(top)
    with open("bundesliga2.txt")as file:
        for i in file:
            nemacki_listbox2.insert(END,i)

    nemacka_labela3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    nemacki_entry=Entry(top)

    def Trofeji_klubova_bundesliga():
        top1=Toplevel()
        top1.title("Trofeji Bundesliga")
        top1.geometry("300x300")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova Bundeslige")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_bundesliga.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_listbox.config(height=15,width=25)
        trofeji_labela.pack()
        trofeji_listbox.pack()

    def Trofeji_klubova_bundesliga2():
        top2=Toplevel()
        top2.title("Trofeji Bundesliga 2")
        top2.geometry("300x300")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klubova Bundeslige2")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_bundesliga2.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15,width=25)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if nemacki_entry.get()=="Bundes liga" or nemacki_entry.get()=="bundes liga":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Bundes liga")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_bundesliga.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if nemacki_entry.get().isdigit()==True:
                raise ValueError

            if nemacki_entry.get()=="":
                raise ValueError

            if nemacki_entry.get()!="Bundes liga" and nemacki_entry.get()!="bundes liga" and nemacki_entry.get()!="Bundes liga 2" and nemacki_entry.get()!="bundes liga 2":
                raise ValueError

            if nemacki_entry.get().isnumeric()==True:
                raise ValueError

            if nemacki_entry.get() == "Bundes liga 2" or nemacki_entry.get() == "bundes liga 2":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Bundesliga 2")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_bundesliga2.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3 = Toplevel()
        top3.title("Online Prodavnica Nemacka")
        top3.geometry("400x435")
        prodavnica_labela = Label(top3, text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox = Listbox(top3)
        prodavnica_listbox2 = Listbox(top3)
        with open("prodavnica_nemacka.txt") as file:
            for i in file:
                prodavnica_listbox.insert(END, i)

        def Korpa():
            try:
                dobijanje = prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END, dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate da izaberete artikal da bi ste ga dodali u korpu!")

        def Kupi_artikle_iz_korpe():
            try:
                kupovina = len(prodavnica_listbox2.get(0, END))
                if kupovina == 0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena", f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje",
                                        "U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje = prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska", "Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme = Button(top3, text="Ukloni artikal iz korpe", command=Ukloni_artikal_iz_korpe)

        def Karte_bundesliga():
            top4 = Toplevel()
            top4.title("Karte za utakmice Bundeslige")
            top4.geometry("300x120")
            karte_labela = Label(top4, text="Izaberite kartu koju zelite da kupite")
            karte_listbox = Listbox(top4)
            with open("karte_bundesliga.txt") as file:
                for i in file:
                    karte_listbox.insert(END, i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4, width=35)

            def Kupovina_karte_bundesliga():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_bundesliga)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_bundesliga2():
            top5 = Toplevel()
            top5.title("Karte za utakmice Bundeslige 2")
            top5.geometry("300x120")
            karte_bundesliga2_labela = Label(top5, text="Izaberite kartu koju zelite da kupite")
            karte_bundesliga2_listbox = Listbox(top5)
            with open("karte_bundesliga2.txt") as file:
                for i in file:
                    karte_bundesliga2_listbox.insert(END, i)

            karte_bundesliga2_labela.pack()
            karte_bundesliga2_listbox.pack()
            karte_bundesliga2_listbox.config(height=4, width=35)

            def Kupovina_karte_bundesliga2():
                try:
                    dobijena_karta=karte_bundesliga2_listbox.get(karte_bundesliga2_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_bundesliga2)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        prodavnica_dugme = Button(top3, text="Dodaj u korpu", command=Korpa)
        prodavnica_dugme2 = Button(top3, text="Kupovina karata za utakmice Bundesliga", command=Karte_bundesliga)
        prodavnica_dugme3 = Button(top3, text="Kupovina karata za utakmice Bundesliga2", command=Karte_bundesliga2)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        prodavnica_dugme.pack()
        korpa_labela.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    nemacko_dugme3=Button(top,text="Prikaz trofeja za klubove Bundeslige",command=Trofeji_klubova_bundesliga)
    nemacko_dugme4=Button(top,text="Prikaz trofeja za klubove Bundeslige 2",command=Trofeji_klubova_bundesliga2)
    nemacko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    nemacko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    nemacki_listbox.config(width=25)
    nemacki_listbox2.config(width=25)
    nemacka_labela.pack()
    nemacki_listbox.pack()
    nemacko_dugme3.pack()
    nemacka_labela2.pack()
    nemacki_listbox2.pack()
    nemacko_dugme4.pack()
    nemacka_labela3.pack()
    nemacki_entry.pack()
    nemacko_dugme6.pack()
    nemacko_dugme5.pack()

def Francuska():
    top=Toplevel()
    top.title("Francuska liga")
    top.geometry("500x510")
    francuska_labela=Label(top,text="Klubovi u Ligi 1")
    francuski_listbox=Listbox(top)
    with open("liga1.txt")as file:
        for i in file:
            francuski_listbox.insert(END,i)

    francuska_labela2=Label(top,text="Klubovi u Ligi 2")
    francuski_listbox2=Listbox(top)
    with open("liga2.txt")as file:
        for i in file:
            francuski_listbox2.insert(END,i)

    francuska_labela3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    francuski_entry=Entry(top)

    def Trofeji_klubova_liga1():
        top1=Toplevel()
        top1.geometry("300x300")
        top1.title("Trofeji Liga 1")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova Lige 1")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_liga1.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_listbox.config(height=15,width=26)
        trofeji_labela.pack()
        trofeji_listbox.pack()

    def Trofeji_klubova_liga2():
        top2=Toplevel()
        top2.geometry("300x300")
        top2.title("Trofeji Liga 2")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klbuova Lige 2")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_liga2.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15,width=26)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if francuski_entry.get()=="Liga 1" or francuski_entry.get()=="liga 1":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Liga 1")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_liga1.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if francuski_entry.get().isdigit()==True:
                raise ValueError

            if francuski_entry.get()=="":
                raise ValueError

            if francuski_entry.get()!="Liga 1" and francuski_entry.get()!="liga 1" and francuski_entry.get()!="Liga 2" and francuski_entry.get()!="liga 2":
                raise ValueError

            if francuski_entry.get().isnumeric()==True:
                raise ValueError

            if francuski_entry.get() == "Liga 2" or francuski_entry.get() == "liga 2":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Liga 2")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_liga2.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3 = Toplevel()
        top3.title("Online Prodavnica Francuska")
        top3.geometry("400x435")
        prodavnica_labela = Label(top3, text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox = Listbox(top3)
        prodavnica_listbox2 = Listbox(top3)
        with open("prodavnica_francuska.txt") as file:
            for i in file:
                prodavnica_listbox.insert(END, i)

        def Korpa():
            try:
                dobijanje = prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END, dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate da izaberete artikal da bi ste ga dodali u korpu!")

        def Kupi_artikle_iz_korpe():
            try:
                kupovina = len(prodavnica_listbox2.get(0, END))
                if kupovina == 0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena", f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje",
                                        "U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje = prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska", "Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme = Button(top3, text="Ukloni artikal iz korpe", command=Ukloni_artikal_iz_korpe)

        def Karte_liga1():
            top4 = Toplevel()
            top4.title("Karte za utakmice Liga 1")
            top4.geometry("300x120")
            karte_labela = Label(top4, text="Izaberite kartu koju zelite da kupite")
            karte_listbox = Listbox(top4)
            with open("karte_liga1.txt") as file:
                for i in file:
                    karte_listbox.insert(END, i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4, width=35)

            def Kupovina_karte_liga1():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_liga1)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_liga2():
            top5 = Toplevel()
            top5.title("Karte za utakmice Liga 2")
            top5.geometry("300x120")
            karte_liga2_labela = Label(top5, text="Izaberite kartu koju zelite da kupite")
            karte_liga2_listbox = Listbox(top5)
            with open("karte_liga2.txt") as file:
                for i in file:
                    karte_liga2_listbox.insert(END, i)

            karte_liga2_labela.pack()
            karte_liga2_listbox.pack()
            karte_liga2_listbox.config(height=4, width=35)

            def Kupovina_karte_liga2():
                try:
                    dobijena_karta=karte_liga2_listbox.get(karte_liga2_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_liga2)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")


        prodavnica_dugme = Button(top3, text="Dodaj u korpu", command=Korpa)
        prodavnica_dugme2 = Button(top3, text="Kupovina karata za utakmice Liga 1", command=Karte_liga1)
        prodavnica_dugme3 = Button(top3, text="Kupovina karata za utakmice Liga 2", command=Karte_liga2)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        prodavnica_dugme.pack()
        korpa_labela.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    francusko_dugme3=Button(top,text="Prikaz trofeja za klubove Lige 1",command=Trofeji_klubova_liga1)
    francusko_dugme4=Button(top,text="Prikaz trofeja za klubove Lige 2",command=Trofeji_klubova_liga2)
    francusko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    francusko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    francuski_listbox.config(width=25)
    francuski_listbox2.config(width=25)
    francuska_labela.pack()
    francuski_listbox.pack()
    francusko_dugme3.pack()
    francuska_labela2.pack()
    francuski_listbox2.pack()
    francusko_dugme4.pack()
    francuska_labela3.pack()
    francuski_entry.pack()
    francusko_dugme6.pack()
    francusko_dugme5.pack()

def Holandija():
    top=Toplevel()
    top.geometry("500x510")
    top.title("Nizozemska liga")
    holandijski_label=Label(top,text="Klubovi u Eredivisie ligi")
    holandijski_listbox=Listbox(top)
    with open("eredivisie.txt")as file:
        for i in file:
            holandijski_listbox.insert(END,i)


    holandijski_label2=Label(top,text="Klubovi u Erstedivisie ligi")
    holandijski_listbox2=Listbox(top)
    with open("erstedivise.txt")as file:
        for i in file:
            holandijski_listbox2.insert(END,i)

    holandijski_label3=Label(top,text="Unesite naziv lige da bi ste videli informacije o predstojecim utakmicama:")
    holandijski_entry=Entry(top)

    def Trofeji_klubova_eredivisie():
        top1=Toplevel()
        top1.geometry("300x300")
        top1.title("Trofeji Eredivisie")
        trofeji_labela=Label(top1,text="Broj trofeja svih klubova Eredivisie")
        trofeji_listbox=Listbox(top1)
        with open("trofeji_eredivisie.txt")as file:
            for i in file:
                trofeji_listbox.insert(END,i)

        trofeji_labela.pack()
        trofeji_listbox.pack()
        trofeji_listbox.config(height=15,width=25)

    def Trofeji_klubova_erstedivisie():
        top2=Toplevel()
        top2.geometry("300x300")
        top2.title("Trofeji Erstedivisie")
        trofeji_labela2=Label(top2,text="Broj trofeja svih klubova Erstedivisie")
        trofeji_listbox2=Listbox(top2)
        with open("trofeji_erstedivisie.txt")as file:
            for i in file:
                trofeji_listbox2.insert(END,i)

        trofeji_listbox2.config(height=15,width=25)
        trofeji_labela2.pack()
        trofeji_listbox2.pack()

    def Raspored_utakmica():
        try:
            if holandijski_entry.get()=="Eredivisie liga" or holandijski_entry.get()=="eredivisie liga":
                top_raspored_utakmica=Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Eredivisie liga")
                top_raspored_utakmica_listbox=Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20,width=60)

                with open("raspored_utakmica_eredivisie.txt")as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END,i)

            if holandijski_entry.get().isdigit()==True:
                raise ValueError

            if holandijski_entry.get()=="":
                raise ValueError

            if holandijski_entry.get()!="Erstedivisie liga" and holandijski_entry.get()!="erstedivisie liga" and holandijski_entry.get()!="Eredivisie liga" and holandijski_entry.get()!="eredivisie liga":
                raise ValueError

            if holandijski_entry.get().isnumeric()==True:
                raise ValueError

            if holandijski_entry.get() == "Erstedivisie liga" or holandijski_entry.get() == "erstedivisie liga":
                top_raspored_utakmica = Toplevel()
                top_raspored_utakmica.title("Raspored utakmica Erstedivisie liga")
                top_raspored_utakmica_listbox = Listbox(top_raspored_utakmica)
                top_raspored_utakmica_listbox.pack()
                top_raspored_utakmica_listbox.config(height=20, width=60)

                with open("raspored_utakmica_erstedivisie.txt") as file:
                    for i in file:
                        top_raspored_utakmica_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Greska","Morate da unesete pravilno naziv lige da bi ste videli raspored utakmica!")

    def Online_prodavnica():
        top3 = Toplevel()
        top3.title("Online Prodavnica Nizozemska")
        top3.geometry("400x435")
        prodavnica_labela = Label(top3, text="Izaberite stavku koju zelite da dodate u korpu")
        korpa_labela = Label(top3, text="Korpa odabranih artikala iz Online Prodavnice")
        prodavnica_listbox = Listbox(top3)
        prodavnica_listbox2 = Listbox(top3)
        with open("prodavnica_nizozemska.txt") as file:
            for i in file:
                prodavnica_listbox.insert(END, i)

        def Korpa():
            try:
                dobijanje = prodavnica_listbox.get(prodavnica_listbox.curselection())
                prodavnica_listbox2.insert(END, dobijanje)

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate da izaberete artikal da bi ste ga dodali u korpu!")

        def Kupi_artikle_iz_korpe():
            try:
                kupovina = len(prodavnica_listbox2.get(0, END))
                if kupovina == 0:
                    raise ValueError

                messagebox.showinfo("Transakcija obavljena", f"Uspesno ste kupili {kupovina} artikla iz korpe! ")

            except ValueError:
                messagebox.showinfo("Obavestenje",
                                        "U korpi mora biti barem jedan artikal da bi ste obavili transakciju!")

        kupovina_artikla_dugme = Button(top3, text="Kupi artikle iz korpe", command=Kupi_artikle_iz_korpe)

        def Ukloni_artikal_iz_korpe():
            try:
                brisanje = prodavnica_listbox2.curselection()
                prodavnica_listbox2.delete(brisanje)

            except Exception:
                messagebox.showerror("Greska", "Niste izabrali artikal da bi ste ga obrisali!")

        brisanje_artikla_dugme = Button(top3, text="Ukloni artikal iz korpe", command=Ukloni_artikal_iz_korpe)

        def Karte_eredivisie():
            top4 = Toplevel()
            top4.title("Karte za utakmice Eredivisie lige")
            top4.geometry("300x120")
            karte_labela = Label(top4, text="Izaberite kartu koju zelite da kupite")
            karte_listbox = Listbox(top4)
            with open("karte_eredivisie.txt") as file:
                for i in file:
                    karte_listbox.insert(END, i)
            karte_labela.pack()
            karte_listbox.pack()
            karte_listbox.config(height=4, width=35)

            def Kupovina_karte_eredivisie():
                try:
                    dobijena_karta=karte_listbox.get(karte_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")
                try:

                    kupovina_dugme=Button(top6,text="Potvrdi",command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska","Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top4, text="Kupi kartu", command=Kupovina_karte_eredivisie)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        def Karte_erstedivisie():
            top5 = Toplevel()
            top5.title("Karte za utakmice Erstedivisie lige")
            top5.geometry("300x120")
            karte_erstedivisie_labela = Label(top5, text="Izaberite kartu koju zelite da kupite")
            karte_erstedivisie_listbox = Listbox(top5)
            with open("karte_erstedivisie.txt") as file:
                for i in file:
                    karte_erstedivisie_listbox.insert(END, i)

            karte_erstedivisie_labela.pack()
            karte_erstedivisie_listbox.pack()
            karte_erstedivisie_listbox.config(height=4, width=35)

            def Kupovina_karte_erstedivisie():
                try:
                    dobijena_karta=karte_erstedivisie_listbox.get(karte_erstedivisie_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Kupovina karata(kolicina)")
                    top6.geometry("300x100")
                    kupovina_label=Label(top6,text="Unesite kolicinu karata koje zelite da kupite")
                    kupovina_entry=Entry(top6)
                    kupovina_label.pack()
                    kupovina_entry.pack()

                except Exception:
                    messagebox.showinfo("Obavestenje","Morate prvo da izaberete kartu!")

                def Kupovina_kolicina():
                    try:
                        if kupovina_entry.get()=="" or kupovina_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Obavestenje",f"Kupili ste {kupovina_entry.get()} karata za {dobijena_karta}")

                    except ValueError:
                        messagebox.showerror("Greska","Morate brojevima da unesete kolicinu karata koje kupujete!")

                try:

                    kupovina_dugme = Button(top6, text="Potvrdi", command=Kupovina_kolicina)
                    kupovina_dugme.pack()

                except Exception:
                    messagebox.showerror("Greska", "Morate prvo da izaberete kartu!")

            try:
                karte_dugme = Button(top5, text="Kupi kartu", command=Kupovina_karte_erstedivisie)
                karte_dugme.pack()

            except Exception:
                messagebox.showinfo("Obavestenje", "Morate prvo da izaberete kartu!")

        prodavnica_dugme = Button(top3, text="Dodaj u korpu", command=Korpa)
        prodavnica_dugme2 = Button(top3, text="Kupovina karata za utakmice Eredivisie", command=Karte_eredivisie)
        prodavnica_dugme3 = Button(top3, text="Kupovina karata za utakmice Erstedivisie", command=Karte_erstedivisie)
        prodavnica_labela.pack()
        prodavnica_listbox.pack()
        prodavnica_dugme.pack()
        korpa_labela.pack()
        prodavnica_listbox2.pack()
        kupovina_artikla_dugme.pack()
        brisanje_artikla_dugme.pack()
        prodavnica_dugme2.pack()
        prodavnica_dugme3.pack()
        prodavnica_listbox.config(height=8, width=35)
        prodavnica_listbox2.config(height=8, width=35)

    holandijsko_dugme3=Button(top,text="Prikaz trofeja za klubove Eredivisie lige",command=Trofeji_klubova_eredivisie)
    holandijsko_dugme4=Button(top,text="Prikaz trofeja za klubove Erstedivisie lige",command=Trofeji_klubova_erstedivisie)
    holandijsko_dugme5=Button(top,text="Online prodavnica",command=Online_prodavnica)
    holandijsko_dugme6=Button(top,text="Prikazi raspored utakmica",command=Raspored_utakmica)

    holandijski_listbox.config(width=25)
    holandijski_listbox2.config(width=25)
    holandijski_label.pack()
    holandijski_listbox.pack()
    holandijsko_dugme3.pack()
    holandijski_label2.pack()
    holandijski_listbox2.pack()
    holandijsko_dugme4.pack()
    holandijski_label3.pack()
    holandijski_entry.pack()
    holandijsko_dugme6.pack()
    holandijsko_dugme5.pack()

root=Tk()
root.title("EuroTop6")
root.geometry("250x165")
a=Button(root,text="Engleska liga",command=Engleska)
a1=Button(root,text="Spanska liga",command=Spanija)
a2=Button(root,text="Italijanska liga",command=Italija)
a3=Button(root,text="Nemacka liga",command=Nemacka)
a4=Button(root,text="Francuska liga",command=Francuska)
a5=Button(root,text="Nizozemska liga",command=Holandija)
a.pack()
a1.pack()
a2.pack()
a3.pack()
a4.pack()
a5.pack()
mainloop()