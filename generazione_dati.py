"""
Script per la generazione di dati utente fittizi utilizzando la libreria Faker.

Questo script crea un elenco di 10 utenti simulati, ognuno con nome, cognome,
email e numero di telefono. I dati sono generati in modo casuale e possono
essere utilizzati per scopi di test o simulazione, senza alcun riferimento
a persone reali.
"""

from faker import Faker

# Inizializzazione di Faker
fake = Faker()

# Generazione di dati fittizi per 10 utenti
user_data = []
for _ in range(10):
    user = {
        "nome": fake.first_name(),
        "cognome": fake.last_name(),
        "email": fake.email(),
        "numero_di_telefono": fake.phone_number()
    }
    user_data.append(user)

# Stampa dei dati generati per verifica
for i, user in enumerate(user_data, 1):
    print(f"Utente {i}: {user}")
