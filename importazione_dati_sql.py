"""
Script per importare i dati da un file Excel in un database SQLite.

Questo script carica i dati degli utenti da un file Excel e li inserisce
in una tabella SQLite, creando il database e la tabella se non esistono.
"""

import sqlite3
import openpyxl

# Caricamento del file Excel con i dati degli utenti
workbook = openpyxl.load_workbook("utenti_fittizi.xlsx")
sheet = workbook["Utenti"]

# Connessione al database SQLite e creazione della tabella
conn = sqlite3.connect("utenti.db")
cursor = conn.cursor()

# Creazione della tabella SQL per archiviare i dati
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cognome TEXT,
        email TEXT,
        numero_di_telefono TEXT
    )
''')

# Inserimento dei dati dal file Excel alla tabella SQL
for row in sheet.iter_rows(min_row=2, values_only=True):
    nome, cognome, email, numero_di_telefono = row
    cursor.execute('''
        INSERT INTO utenti (nome, cognome, email, numero_di_telefono)
        VALUES (?, ?, ?, ?)
    ''', (nome, cognome, email, numero_di_telefono))

# Salvataggio delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Dati degli utenti importati con successo nel database SQLite.")
