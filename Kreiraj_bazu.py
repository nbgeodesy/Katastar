import sqlite3
from sqlite3 import Error

class Parcele:
    def __init__(self, id_parcele, br_parcele, pbr_parcele, kultura, klasa, pov, plan, skica, broj_pl):
        self.id_parcele = id_parcele
        self.br_parcele = br_parcele
        self.pbr_parcele = pbr_parcele
        self.kultura = kultura
        self.klasa = klasa
        self.pov = pov
        self.plan = plan
        self.skica = skica
        self.broj_pl = broj_pl
    def __str__(self):
        return str(self.br_parcele) + str(self.pbr_parcele) + self.kultura + str(self.klasa) + str(self.pov) + str(self.plan) + str(self.skica)

class Posjednici:
    def __init__(self, broj_pl, ime, prezime, jmbg, vrsta_prava, obim_prava):
        self.broj_pl = broj_pl
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.vrsta_prava = vrsta_prava
        self.obim_prava = obim_prava
    def __str__(self):
        return self.pl + self.ime + self.prezime + str(self.jmbg) + self.vrsta_prava + str(self.obim_prava) + str(self.id_parcele)

class PosList:
    def __init__(self, id_pl, broj_pl):
        self.id_pl = id_pl
        self.broj = broj_pl
    def __str__(self):
        return 'Broj PLa \t' + 'Posjednik \t' + 'Parcela' + '\n' +str(self.broj)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        kursor = conn.cursor()
        kursor.execute(create_table_sql)
    except Error as e:
        print(e)

def dodaj_parcelu(conn, parcela):
    try:
        unos = """INSERT INTO parcele(id_parcele, br_parcele, pbr_parcele, kultura, klasa, pov, plan, skica, broj_pl)
         VALUES (?,?,?,?,?,?,?,?, ?)"""
        cur = conn.cursor()
        parametri = (parcela.id_parcele, parcela.br_parcele, parcela.pbr_parcele, parcela.kultura, parcela.klasa, parcela.pov, parcela.plan, parcela.skica, parcela.broj_pl)
        cur.execute(unos, parametri)
        conn.commit()
    except Error as e:
        print(e)

def dodaj_posjednika(conn, posjednik):
    try:
        unos = """INSERT INTO posjednici(broj_pl, ime, prezime, jmbg, vrsta_prava, obim_prava)
        VALUES (?, ?, ?, ?, ?, ?)"""
        cur = conn.cursor()
        parametri = (posjednik.broj_pl, posjednik.ime, posjednik.prezime, posjednik.jmbg, posjednik.vrsta_prava, posjednik.obim_prava)
        cur.execute(unos, parametri)
        conn.commit()
    except Error as e:
        print(e)

def dodaj_pos_list(conn, pos_list):
    try:
        unos = """INSERT INTO pos_list(id_pl, broj_pl)
                VALUES (?, ?)"""
        cur = conn.cursor()
        parametri = (pos_list.id_pl, pos_list.broj)
        cur.execute(unos, parametri)
        conn.commit()
    except Error as e:
        print(e)

def prikaz(conn):
    try:
        upit = '''SELECT posjednici.broj_pl, posjednici.ime, posjednici.prezime, posjednici.jmbg, posjednici.vrsta_prava, posjednici.obim_prava, parcele.br_parcele, parcele.pbr_parcele, parcele.kultura, parcele.klasa, parcele.pov
         FROM parcele, posjednici WHERE posjednici.broj_pl = parcele.broj_pl;'''
        cur = conn.cursor()
        cur.execute(upit)
        prikazi = cur.fetchall()
        return prikazi
    except Error as e:
        print(e)

def azuriraj_posjednika(conn, ime, jmbg):
    try:
        azuriraj_posjednika = '''UPDATE posjednici
                                 SET ime = ?
                                  WHERE jmbg = ?'''
        cur = conn.cursor()
        parametri = (ime, jmbg)
        cur.execute(azuriraj_posjednika, parametri)
        conn.commit()
    except Error as e:
        print(e)
def azuriraj_parcelu(conn, br_parcele, pbr_parcele, id_parcele):
    try:
        azuriraj_parcelu = '''UPDATE parcele 
                            SET br_parcele = ?, pbr_parcele = ?
                            WHERE id_parcele = ?'''
        cur = conn.cursor()
        parametri = (br_parcele, pbr_parcele, id_parcele)
        cur.execute(azuriraj_parcelu, parametri)
        conn.commit()
    except Error as e:
        print(e)

def izbrisi_parcelu(conn, brp, pbrp):
    try:
        izbrisi_parcelu = '''DELETE FROM parcele
                        WHERE br_parcele = ? AND pbr_parcele = ?'''
        cur = conn.cursor()
        parametri = (brp, pbrp)
        cur.execute(izbrisi_parcelu, parametri,)
        conn.commit()
    except Error as e:
        print(e)