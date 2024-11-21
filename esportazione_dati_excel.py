"""
Script per esportare dati fittizi in un file Excel utilizzando la libreria openpyxl.

Il file generato contiene un elenco di utenti con i seguenti campi:
- Nome
- Cognome
- Email
- Numero di Telefono
"""

import openpyxl

# Dati fittizi per 10 utenti
user_data = [
    {"nome": "Mario", "cognome": "Rossi", "email": "mario.rossi@example.com", "numero_di_telefono": "+39 333 1234567"},
    {"nome": "Luca", "cognome": "Bianchi", "email": "luca.bianchi@example.com", "numero_di_telefono": "+39 333 2345678"},
    {"nome": "Giulia", "cognome": "Verdi", "email": "giulia.verdi@example.com", "numero_di_telefono": "+39 333 3456789"},
    {"nome": "Anna", "cognome": "Neri", "email": "anna.neri@example.com", "numero_di_telefono": "+39 333 4567890"},
    {"nome": "Marco", "cognome": "Gialli", "email": "marco.gialli@example.com", "numero_di_telefono": "+39 333 5678901"},
    {"nome": "Sara", "cognome": "Blu", "email": "sara.blu@example.com", "numero_di_telefono": "+39 333 6789012"},
    {"nome": "Francesca", "cognome": "Grigi", "email": "francesca.grigi@example.com", "numero_di_telefono": "+39 333 7890123"},
    {"nome": "Alessandro", "cognome": "Rosa", "email": "alessandro.rosa@example.com", "numero_di_telefono": "+39 333 8901234"},
    {"nome": "Elena", "cognome": "Viola", "email": "elena.viola@example.com", "numero_di_telefono": "+39 333 9012345"},
    {"nome": "Davide", "cognome": "Marroni", "email": "davide.marroni@example.com", "numero_di_telefono": "+39 333 0123456"}
]

# Creazione di un file Excel e inserimento dei dati
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Utenti"

# Aggiunta dell'intestazione delle colonne
headers = ["Nome", "Cognome", "Email", "Numero di Telefono"]
sheet.append(headers)

# Aggiunta dei dati degli utenti
for user in user_data:
    sheet.append([user["nome"], user["cognome"], user["email"], user["numero_di_telefono"]])

# Salvataggio del file Excel
workbook.save("utenti_fittizi.xlsx")
print("File Excel creato con i dati degli utenti fittizi.")
