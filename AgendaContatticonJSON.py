import json
import os

def aggiungi_contatto(agenda, nome, telefono, email, citta=""):
    """Aggiunge contatto all'agenda"""
    agenda[nome] = {
        "telefono": telefono,
        "email": email,
        "citta": citta
    }
    print(f"✓ Contatto '{nome}' aggiunto")

def rimuovi_contatto(agenda, nome):
    """Rimuove contatto dall'agenda"""
    if nome in agenda:
        del agenda[nome]
        print(f"✓ Contatto '{nome}' rimosso")
        return True
    else:
        print(f"✗ Contatto '{nome}' non trovato")
        return False

def cerca_contatto(agenda, nome):
    """Cerca contatto per nome (parziale, case-insensitive)"""
    risultati = {}
    nome_lower = nome.lower()
    
    for nome_contatto, dati in agenda.items():
        if nome_lower in nome_contatto.lower():
            risultati[nome_contatto] = dati
    
    return risultati

def modifica_contatto(agenda, nome, **kwargs):
    """Modifica campi di un contatto esistente"""
    if nome not in agenda:
        print(f"✗ Contatto '{nome}' non trovato")
        return False
    
    for campo, valore in kwargs.items():
        if campo in ["telefono", "email", "citta"]:
            agenda[nome][campo] = valore
            print(f"✓ {campo.capitalize()} di '{nome}' aggiornato")
        else:
            print(f"✗ Campo '{campo}' non valido")
    
    return True

def lista_per_citta(agenda, citta):
    """Restituisce contatti di una città"""
    risultati = {}
    citta_lower = citta.lower()
    
    for nome, dati in agenda.items():
        if dati.get("citta", "").lower() == citta_lower:
            risultati[nome] = dati
    
    return risultati

def salva_agenda(agenda, filename="agenda.json"):
    """Salva agenda su file JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(agenda, f, indent=2, ensure_ascii=False)
        print(f"✓ Agenda salvata in: {filename}")
        return True
    except Exception as e:
        print(f"✗ Errore salvataggio: {e}")
        return False

def carica_agenda(filename="agenda.json"):
    """Carica agenda da file JSON"""
    if not os.path.exists(filename):
        print(f"File '{filename}' non trovato. Creata agenda vuota.")
        return {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            agenda = json.load(f)
        print(f"✓ Agenda caricata da: {filename}")
        print(f"  {len(agenda)} contatti trovati")
        return agenda
    except Exception as e:
        print(f"✗ Errore caricamento: {e}")
        return {}

def stampa_contatto(nome, dati):
    """Formatta output contatto"""
    citta = dati.get("citta", "N/A")
    return f"{nome}: {dati['telefono']}, {dati['email']}, {citta}"

def stampa_agenda(agenda):
    """Stampa agenda completa"""
    if not agenda:
        print("Agenda vuota")
        return
    
    print(f"\n{'='*60}")
    print(f"AGENDA CONTATTI ({len(agenda)} contatti)".center(60))
    print('='*60)
    
    for nome in sorted(agenda.keys()):
        print(f"  {stampa_contatto(nome, agenda[nome])}")
    
    print('='*60)

# Test
print("=== AGENDA CONTATTI ===\n")

# Crea agenda
agenda = {}
aggiungi_contatto(agenda, "Mario Rossi", "333-1234567", "mario.rossi@email.com", "Roma")
aggiungi_contatto(agenda, "Anna Verdi", "339-7654321", "anna.verdi@email.com", "Milano")
aggiungi_contatto(agenda, "Luca Bianchi", "345-9876543", "luca.bianchi@email.com", "Roma")

# Stampa agenda
stampa_agenda(agenda)

# Cerca
print("\nContatti in Roma:")
roma = lista_per_citta(agenda, "Roma")
for nome, dati in roma.items():
    print(f"  - {stampa_contatto(nome, dati)}")

# Modifica
print("\nModifica contatto:")
modifica_contatto(agenda, "Mario Rossi", telefono="333-9999999", citta="Napoli")

# Salva
salva_agenda(agenda, "contatti.json")

# Carica
print("\nTest caricamento:")
agenda_caricata = carica_agenda("contatti.json")