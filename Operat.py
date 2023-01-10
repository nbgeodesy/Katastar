import uuid
import Kreiraj_bazu

#Kreiranje baze podataka
konekcija = Kreiraj_bazu.create_connection('operat.db')

#Kreiranje tabela u okviru baze podataka
kreiraj_tabelu_parcele = '''CREATE TABLE IF NOT EXISTS parcele (
id_parcele VARCHAR PRIMARY KEY,
br_parcele INTEGER,
pbr_parcele INTEGER,
kultura VARCHAR(15),
klasa INTEGER,
pov FLOAT,
plan INTEGER,
skica INTEGER,
broj_pl INTEGER NOT NULL,
FOREIGN KEY (broj_pl)
    REFERENCES pos_list(broj_pl));'''
parcele = Kreiraj_bazu.create_table(konekcija, kreiraj_tabelu_parcele)

kreiraj_tabelu_posjednici = '''CREATE TABLE IF NOT EXISTS posjednici (
broj_pl INTEGER NOT NULL,
jmbg INTEGER PRIMARY KEY,
ime VARCHAR,
prezime VARCHAR,
vrsta_prava VARCHAR,
obim_prava VARCHAR,
FOREIGN KEY (broj_pl)
    REFERENCES pos_list(broj_pl));'''
posjednici = Kreiraj_bazu.create_table(konekcija, kreiraj_tabelu_posjednici)

kreiraj_pos_list = '''CREATE TABLE IF NOT EXISTS pos_list(
id_pl VARCHAR,
broj_pl INTEGER PRIMARY KEY);'''
pos_list = Kreiraj_bazu.create_table(konekcija,kreiraj_pos_list)

#Unos podataka u tabele
while True:
    glavni_meni = input('DOBRODOSLI U PROGRAM KATASTARSKI OPERAT! \n Glavni meni: \n Unos podataka o posjednovnom listu - U \n Prikaz unesenih podataka - P \n Azuriranje podataka - A \n Brisanje parcela - B \n Eksport podataka u CSV datoteku - C \n Izlaz iz programa - I : \n ')
    glavni_meni = glavni_meni.upper()

    if glavni_meni == 'U':
        broj_pl = input('Unesite broj posjednovnog lista: ')
        id_pl = uuid.uuid4().int
        id_pl = str(id_pl)

        pos_list = Kreiraj_bazu.PosList(id_pl, broj_pl)
        dodaj_pos_list = Kreiraj_bazu.dodaj_pos_list(konekcija, pos_list)

        while True:
            pomocni_meni = int(input('Za unos podataka o posjedniku unesite 1, za unos podataka o parcelama unesite 2,'
                                     'za korak nazad unesite 3!: '))

            if pomocni_meni == 1:
                br_posjednika = int(input('Koliko posjednika zelite unijeti? '))
                while br_posjednika > 0:
                    broj_pl = int(input('Unesite broj PLa: '))
                    ime = input('Unesite ime posjednika: ')
                    ime = ime.upper()
                    prezime = input('Unesite prezime posjednika: ')
                    prezime = prezime.upper()
                    jmbg = int(input('Unesite maticni broj posjednika: '))
                    vrsta_prava = input('Unesite vrstu prava: ')
                    vrsta_prava.upper()
                    obim_prava = input('Unesite obim prava u obliku npr 1/1: ')

                    br_posjednika -= 1

                    posjednik = Kreiraj_bazu.Posjednici(broj_pl, ime, prezime, jmbg, vrsta_prava, obim_prava)
                    dodaj_posjednika = Kreiraj_bazu.dodaj_posjednika(konekcija, posjednik)


            elif pomocni_meni == 2:
                br_parcela = int(input('Koliko parcela zelite unijeti? '))
                while br_parcela > 0:
                    id_parcele = uuid.uuid4().int
                    id_parcele = str(id_parcele)
                    br_parcele = int(input('Unesite broj parcele: '))
                    pbr_parcele = int(input('Unesite podbroj parcele: '))
                    kultura = input('Unesite kulturu parcele: ')
                    klasa = int(input('Unesite klasu: '))
                    pov = float(input('Unesite povrsinu parcele: '))
                    plan = int(input('Unesite broj plana: '))
                    skica = int(input('Unesite broj skice: '))
                    broj_pla = broj_pl
                    br_parcela -= 1
                    parcela = Kreiraj_bazu.Parcele(id_parcele, br_parcele, pbr_parcele, kultura, klasa, pov, plan, skica, broj_pla)
                    dodaj_parcelu = Kreiraj_bazu.dodaj_parcelu(konekcija, parcela)

            elif pomocni_meni == 3:
                False
                print('Vratili ste se korak nazad!')
                break

            else:
                print('pogresan unos, unesite jednu od ponudjenih opcija!')
    elif glavni_meni == 'P':
        print('PL   IME     PREZIME     JMBG    VSRTA_PRAVA     OBIM_PRAVA      BR_PARCELE  PBR_PARCELE     KULTURA     KLASA   POVRSINA')
        prikaz = Kreiraj_bazu.prikaz(konekcija)
        for i in prikaz:
            print(*i, sep='     ')

    elif glavni_meni == 'A':
        while True:
            azuriraj = int(input('Za azuriranje posjednika unesite 1, za azuriranje parcele unesite 2, za korak nazad unesite 3: '))
            if azuriraj == 1:
                azuriranje_jmbg = int(input('Unesite maticni broj, cije ime zelite izmjeniti: '))
                azuriranje_ime = input('Unesite novo ime posjednika: ')
                update_posjednika = Kreiraj_bazu.azuriraj_posjednika(konekcija, azuriranje_ime, azuriranje_jmbg)
            elif azuriraj == 2:
                azuriranje_idparcele = input('Unesite id parcele za koju zelite azurirati broj i podbroj parcele: ')
                azuriranje_brp = int(input('Unesite novi broj parcele: '))
                azuriranje_pbrp = int(input('Unesite novi podbroj parcele: '))
                update_parcele = Kreiraj_bazu.azuriraj_parcelu(konekcija, azuriranje_brp, azuriranje_pbrp, azuriranje_idparcele)
            elif azuriraj == 3:
                False
                print('Vratili ste se korak nazad!')
                break
            else:
                print('pogresan unos, unesite jednu od ponudjenih opcija!')
                azuriraj = int(input('Za azuriranje posjednika, unesite 1, za azuriranje parcele unesite 2, za korak nazad unesite 3: '))
    elif glavni_meni == 'B':
        brp_brisanje = int(input('Unesite broj parcele koju zelite izbrisati: '))
        pbrp_brisanje = int(input('Unesite podbroj parcele '))
        izbrisi_parcelu = Kreiraj_bazu.izbrisi_parcelu(konekcija, brp_brisanje, pbrp_brisanje)

    elif glavni_meni == 'I':
        False
        print('Izasli ste iz programa!')
        break
    else:
        print('Greska unosa! ')
        glavni_meni = input('Za unos podataka o posjednovnom listu unesite U, za izlaz iz programa unesite I !: ')
        glavni_meni = glavni_meni.upper()













    







