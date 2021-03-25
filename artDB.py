import os
import sqlite3

def create_database():

    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()

    # tworzenie tabeli

    cursor.execute("""create table kluby

    (nazwa text, trener text, kraj text, liczba_piłkarzy int, najlepszy_zawodnik int, sponsor_glowny text)

    """)

    # insert

    cursor.execute("INSERT INTO kluby VALUES "

    "('Michał', 'Probierz', 'Polska', '20', '1', 'pryncypałki')")

    # zapisanie danych do bazy

    conn.commit()


def delete_database():

    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()

    cursor.execute("""DELETE FROM kluby WHERE nazwa""")


    conn.close()


def update_database(nazwa, new_trener):


    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()

    sql = "UPDATE kluby SET trener = ? where nazwa = ?"

    cursor.execute(sql, (new_trener, nazwa))

    cursor.close()



def select_all_albums(trener):

    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()

    sql = "SELECT * FROM kluby WHERE trener=?"

    cursor.execute(sql, [(trener)])

    result = cursor.fetchall()

    cursor.close()

    conn.close()

    return result

if __name__ == '__main__':

    if not os.path.exists("mydatabase.db"):
        create_database()
    print(select_all_albums('Michał’))