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