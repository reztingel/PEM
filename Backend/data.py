import sqlite3

con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS brukere(
            id integer primay key NOT NULL;
            navn text NOT NULL,
            passord text NOT NULL
            )""")
con.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS resturanger(
            id integer primary key NOT NULL,
            navn text NOT NULL
            )""")
con.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS meny_retter(
            retter_id integer primary key NOT NULL,
            resturang_id integer NOT NULL,
            rett text NOT NULL,
            bilde text NOT NULL,
            beskrivelse text NOT NULL,
            pris integer NOT NULL
            )""")
con.commit()

brukere = ["REST1", "REST2", "REST3"]
resturanger = [{"navn": "PAsTA", "id": 1}, {"navn": "TACO", "id": 2}]


meny1 = [{"rid": 1, "rett": "Kjøttboler", "bilde": "kjøttboller.jpg", "beskrivelse": "kjøttboller med saus og poteter", "pris": 20},
         {"rid": 1, "rett": "pizza", "bilde": "pizza.jpg", "beskrivelse": "pizza med saus og pepperoni og ost", "pris": 45},
         {"rid": 1, "rett": "hamburger", "bilde": "burger.jpg", "beskrivelse": "hamburger med ost", "pris": 30},
         {"rid": 1, "rett": "fish n chips", "bilde": "fish_chips.jpg", "beskrivelse": "fish n chips med fish n chips", "pris": 40},
         {"rid": 1, "rett": "pasta", "bilde": "pasta.jpg", "beskrivelse": "pasta med pølse bitter", "pris": 30}]


cur.execute("DELETE FROM brukere")
cur.execute("DELETE FROM resturanger")
cur.execute("DELETE FROM meny_retter")
con.commit()
cur.executemany("INSERT INTO brukere(navn, passord) VALUES(?, 'Passord')", [(bruker,) for bruker in brukere])
cur.executemany("INSERT INTO resturanger(id,navn) VALUES(?,?)", [(rest["id"], rest["navn"]) for rest in resturanger])
cur.executemany("INSERT INTO meny_retter(resturang_id, rett, bilde, beskrivelse, pris) VALUES(?,?,?,?,?)", [(rett["rid"], rett["rett"], rett["bilde"], rett["beskrivelse"], rett["pris"]) for rett in meny1])
con.commit()