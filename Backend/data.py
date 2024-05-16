import sqlite3


con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS brukere(
            ID INTEGER PRIMARY KEY,
            navn text NOT NULL,
            passord text NOT NULL
            )""")
con.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS resturanger(
            ID INTEGER PRIMARY KEY,
            navn TEXT 
            )""")
con.commit()



cur.execute("""CREATE TABLE IF NOT EXISTS meny_retter(
            retter_id INTEGER PRIMARY KEY,
            resturang_id INTEGER NOT NULL,
            rett text NOT NULL,
            bilde text NOT NULL,
            beskrivelse text NOT NULL,
            pris integer NOT NULL
            )""")
con.commit()


brukere = ["REST1", "REST2", "REST3"]
resturanger = [{"navn": "PAsTA", "id":1}, {"navn": "TACO", "id":2}]


meny1 = [{"id":1, "rett": "Kjøttboler", "bilde": "kjøttboller.jpg", "beskrivelse": "kjøttboller med saus og poteter", "pris": 20},
         {"id":2, "rett": "pizza", "bilde": "pizza.jpg", "beskrivelse": "pizza med saus og pepperoni og ost", "pris": 45},
         {"id":1, "rett": "hamburger", "bilde": "burger.jpg", "beskrivelse": "hamburger med ost", "pris": 30},
         {"id":2, "rett": "fish n chips", "bilde": "fish-and-chips.jpg", "beskrivelse": "fish n chips med fish n chips", "pris": 40},
         {"id":1, "rett": "pasta", "bilde": "pasta.jpg", "beskrivelse": "pasta med pølse bitter", "pris": 30}]


cur.execute("DELETE FROM brukere")
cur.execute("DELETE FROM resturanger")
cur.execute("DELETE FROM meny_retter")
con.commit()
cur.executemany("INSERT INTO brukere(navn, passord) VALUES(?, 'Passord')", [(bruker,) for bruker in brukere])
cur.executemany("INSERT INTO resturanger(navn) VALUES(?)", [(rest["navn"],) for rest in resturanger])
cur.executemany("INSERT INTO meny_retter(resturang_id,rett,bilde, beskrivelse, pris) VALUES(?,?,?,?,?)",[(rett["id"],rett["rett"],rett["bilde"],rett["beskrivelse"],rett["pris"]) for rett in meny1])
con.commit()
con.close()