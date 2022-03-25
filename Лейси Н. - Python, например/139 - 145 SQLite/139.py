import sqlite3

with sqlite3.connect('PhoneBook.db') as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS telefoane(
                ID integer,
                First_Name text NOT NULL,
                Surename text NOT NULL,
                Phone_Number integer);''')

cursor.execute("""INSERT INTO telefoane(ID, First_Name, Surename, Phone_Number)
                 VALUES ('2', 'Colea', 'Moconu', '078474578')""")

cursor.execute("DELETE FROM telefoane WHERE ID=2")

db.commit()
