# LEZIONE 26 - ESERCITAZIONI
## Ripasso Python Base e Strutture Dati

**Modalità:** Individuale | **Durata:** 2 ore (60 min guidate + 60 min autonome)

---

## 📋 ESERCITAZIONI GUIDATE (60 minuti)

### Esercizio 1 - Gestione Lista Studenti (20 minuti)

#### Descrizione
Creare un programma che gestisce una lista di studenti rappresentati come dizionari. Ogni studente ha: nome, matricola, corso e lista voti.

#### Requisiti
1. Creare una lista con almeno 3 studenti
2. Implementare funzione `aggiungi_studente(lista, nome, matricola, corso)`
3. Implementare funzione `aggiungi_voto(lista, matricola, voto)`
4. Implementare funzione `calcola_media(lista, matricola)` che restituisce la media voti
5. Implementare funzione `studenti_per_corso(lista, corso)` che restituisce tutti gli studenti di un corso

#### Struttura Dati Suggerita
```python
studente = {
    "nome": "Mario Rossi",
    "matricola": "12345",
    "corso": "Informatica",
    "voti": [28, 30, 27]
}
```

#### Output Atteso
```
Studenti in Informatica:
- Mario Rossi (12345): media 28.33
- Anna Verdi (12346): media 29.00

Media Mario Rossi: 28.33
```

#### Hint
- Usa `append()` per aggiungere elementi alle liste
- Per la media: `sum(voti) / len(voti)`
- Per filtrare per corso, usa un ciclo `for` e controlla `if studente["corso"] == corso`

---

### Esercizio 2 - Analisi Testo (20 minuti)

#### Descrizione
Scrivere un programma che analizza un testo e fornisce statistiche varie.

#### Requisiti
1. Funzione `conta_parole(testo)` - restituisce numero totale di parole
2. Funzione `conta_caratteri(testo)` - restituisce numero caratteri (esclusi spazi)
3. Funzione `parola_piu_lunga(testo)` - restituisce la parola più lunga
4. Funzione `frequenza_parole(testo)` - restituisce dizionario con frequenza di ogni parola
5. Funzione `parola_piu_frequente(testo)` - restituisce la parola che appare più volte

#### Testo di Test
```python
testo = """Python è un linguaggio di programmazione potente e facile da imparare.
Ha strutture dati efficienti e un approccio semplice ma efficace alla programmazione orientata agli oggetti."""
```

#### Output Atteso
```
Numero parole: 26
Numero caratteri: 134
Parola più lunga: programmazione
Parola più frequente: programmazione (appare 2 volte)

Frequenze:
python: 1
è: 1
un: 2
linguaggio: 1
...
```

#### Hint
- Usa `testo.split()` per dividere in parole
- Usa `lower()` per rendere case-insensitive
- Usa dizionario per contare frequenze: `freq[parola] = freq.get(parola, 0) + 1`
- Per trovare massimo: `max(dict, key=dict.get)`

---

### Esercizio 3 - Generatore Password Sicure (20 minuti)

#### Descrizione
Creare un generatore di password casuali con opzioni di personalizzazione e verifica di complessità.

#### Requisiti
1. Funzione `genera_password(lunghezza, maiuscole=True, numeri=True, simboli=True)`
   - Genera password casuale con caratteri richiesti
   - Default: include tutto
   
2. Funzione `verifica_complessita(password)` che restituisce dizionario con:
   - `lunghezza_ok`: True se >= 8 caratteri
   - `ha_maiuscole`: True se contiene almeno una maiuscola
   - `ha_minuscole`: True se contiene almeno una minuscola
   - `ha_numeri`: True se contiene almeno un numero
   - `ha_simboli`: True se contiene almeno un simbolo
   - `sicura`: True se soddisfa tutti i criteri

3. Funzione `genera_password_sicura()` che genera password finché non è sicura

#### Caratteri Disponibili
```python
import string
minuscole = string.ascii_lowercase  # 'abcd...xyz'
maiuscole = string.ascii_uppercase  # 'ABCD...XYZ'
numeri = string.digits             # '0123456789'
simboli = '!@#$%^&*()_+-=[]{}|;:,.<>?'
```

#### Output Atteso
```
Password generata: K7$mPq2@Xw
Verifica complessità:
  Lunghezza OK: ✓
  Ha maiuscole: ✓
  Ha minuscole: ✓
  Ha numeri: ✓
  Ha simboli: ✓
  Password sicura: ✓

Nuova password sicura: Tr9#Lp5&Mn
```

#### Hint
- Usa `random.choice(caratteri)` per scegliere carattere casuale
- Usa `any(c.isupper() for c in password)` per verificare maiuscole
- Costruisci stringa caratteri disponibili concatenando le categorie richieste

---

## 🎯 ESERCITAZIONI AUTONOME (60 minuti)

### Esercizio 4 - Sistema Gestione Prodotti (20 minuti)

#### Descrizione
Creare un sistema per gestire l'inventario di un negozio.

#### Requisiti
Ogni prodotto è un dizionario con: `id`, `nome`, `categoria`, `prezzo`, `quantita`.

Implementare le seguenti funzioni:

1. `aggiungi_prodotto(inventario, id, nome, categoria, prezzo, quantita)`
   - Aggiunge prodotto alla lista inventario

2. `rimuovi_prodotto(inventario, id)`
   - Rimuove prodotto per ID

3. `cerca_prodotto(inventario, nome)`
   - Restituisce tutti i prodotti che contengono `nome` nel loro nome (case-insensitive)

4. `prodotti_per_categoria(inventario, categoria)`
   - Restituisce lista prodotti di una categoria

5. `valore_totale_inventario(inventario)`
   - Restituisce valore totale (somma di prezzo * quantita per ogni prodotto)

6. `prodotti_sotto_scorta(inventario, soglia=10)`
   - Restituisce prodotti con quantità < soglia

#### Dati di Test
```python
inventario = [
    {"id": 1, "nome": "Laptop Dell", "categoria": "Elettronica", "prezzo": 800, "quantita": 5},
    {"id": 2, "nome": "Mouse Logitech", "categoria": "Elettronica", "prezzo": 25, "quantita": 50},
    {"id": 3, "nome": "Sedia Ergonomica", "categoria": "Arredamento", "prezzo": 200, "quantita": 8},
    {"id": 4, "nome": "Scrivania", "categoria": "Arredamento", "prezzo": 350, "quantita": 3}
]
```

#### Output Atteso
```
Valore totale inventario: €6,850.00

Prodotti sotto scorta (< 10):
- Laptop Dell: 5 unità
- Sedia Ergonomica: 8 unità
- Scrivania: 3 unità

Ricerca "dell": 
- Laptop Dell (Elettronica): €800.00 x 5

Categoria Elettronica:
- Laptop Dell: €800.00 x 5
- Mouse Logitech: €25.00 x 50
```

---

### Esercizio 5 - Agenda Contatti con JSON (20 minuti)

#### Descrizione
Creare un'agenda contatti con salvataggio e caricamento da file JSON.

#### Requisiti

1. `aggiungi_contatto(agenda, nome, telefono, email, citta="")`
   - Aggiunge contatto al dizionario agenda (nome come chiave)

2. `rimuovi_contatto(agenda, nome)`
   - Rimuove contatto per nome

3. `cerca_contatto(agenda, nome)`
   - Cerca contatto per nome (case-insensitive, anche parziale)

4. `modifica_contatto(agenda, nome, **kwargs)`
   - Modifica campi esistenti di un contatto
   - Esempio: `modifica_contatto(agenda, "Mario", telefono="333-1234567")`

5. `lista_per_citta(agenda, citta)`
   - Restituisce tutti i contatti di una città

6. `salva_agenda(agenda, filename)`
   - Salva agenda in file JSON

7. `carica_agenda(filename)`
   - Carica agenda da file JSON
   - Restituisce dizionario vuoto se file non esiste

#### Struttura Dati
```python
agenda = {
    "Mario Rossi": {
        "telefono": "333-1234567",
        "email": "mario.rossi@email.com",
        "citta": "Roma"
    },
    "Anna Verdi": {
        "telefono": "339-7654321",
        "email": "anna.verdi@email.com",
        "citta": "Milano"
    }
}
```

#### Output Atteso
```
Contatti in Roma:
- Mario Rossi: 333-1234567, mario.rossi@email.com

Agenda salvata in: contatti.json

Agenda caricata da file:
2 contatti trovati.
```

#### Hint JSON
```python
import json

# Salvataggio
with open(filename, 'w') as f:
    json.dump(agenda, f, indent=2)

# Caricamento
with open(filename, 'r') as f:
    agenda = json.load(f)
```

---

### Esercizio 6 - Challenge: Analisi Dati Vendite (20 minuti)

#### Descrizione
Analizzare dati di vendite e produrre statistiche e report.

#### Dati di Input
Lista di vendite (simula CSV):
```python
vendite = [
    {"data": "2025-01-15", "prodotto": "Laptop", "categoria": "Elettronica", "quantita": 2, "prezzo_unitario": 800},
    {"data": "2025-01-15", "prodotto": "Mouse", "categoria": "Elettronica", "quantita": 5, "prezzo_unitario": 25},
    {"data": "2025-01-16", "prodotto": "Sedia", "categoria": "Arredamento", "quantita": 3, "prezzo_unitario": 200},
    {"data": "2025-01-16", "prodotto": "Laptop", "categoria": "Elettronica", "quantita": 1, "prezzo_unitario": 800},
    {"data": "2025-01-17", "prodotto": "Scrivania", "categoria": "Arredamento", "quantita": 1, "prezzo_unitario": 350},
    {"data": "2025-01-17", "prodotto": "Mouse", "categoria": "Elettronica", "quantita": 10, "prezzo_unitario": 25}
]
```

#### Requisiti

1. `fatturato_totale(vendite)`
   - Restituisce somma di (quantita * prezzo_unitario) per tutte le vendite

2. `vendite_per_categoria(vendite)`
   - Restituisce dizionario {categoria: fatturato_totale}

3. `prodotto_piu_venduto(vendite)`
   - Restituisce nome prodotto con maggior quantità venduta (somma)

4. `fatturato_per_giorno(vendite)`
   - Restituisce dizionario {data: fatturato}

5. `statistiche_complete(vendite)` che restituisce dizionario con:
   - `fatturato_totale`
   - `numero_transazioni`
   - `fatturato_medio_per_transazione`
   - `categoria_top` (con maggior fatturato)
   - `prodotto_piu_venduto`
   - `giorno_migliore` (con maggior fatturato)

6. `filtra_per_categoria(vendite, categoria)`
   - Restituisce solo vendite di una categoria

7. `vendite_sopra_soglia(vendite, soglia)`
   - Restituisce vendite con fatturato (quantita * prezzo) > soglia

#### Output Atteso
```
=== REPORT VENDITE ===

Fatturato totale: €3,775.00
Numero transazioni: 6
Fatturato medio per transazione: €629.17

Vendite per categoria:
- Elettronica: €2,775.00 (73.5%)
- Arredamento: €1,000.00 (26.5%)

Prodotto più venduto: Mouse (15 unità)
Categoria top: Elettronica
Giorno migliore: 2025-01-15 (€1,725.00)

Fatturato per giorno:
- 2025-01-15: €1,725.00
- 2025-01-16: €1,400.00
- 2025-01-17: €650.00

Vendite sopra €500:
- 2025-01-15: Laptop (€1,600.00)
- 2025-01-16: Sedia (€600.00)
- 2025-01-16: Laptop (€800.00)
```

#### Hint Avanzati
- Usa dizionari per aggregare dati
- `from collections import defaultdict` può semplificare aggregazioni
- Per percentuali: `(valore / totale) * 100`
- Per ordinare dizionario: `sorted(dict.items(), key=lambda x: x[1], reverse=True)`

---

## 📝 NOTE PER LO STUDENTE

### Suggerimenti Generali
- **Testa frequentemente**: Esegui il codice dopo ogni funzione implementata
- **Usa print per debug**: `print(f"Valore variabile: {var}")` aiuta a capire cosa succede
- **Funzioni piccole**: Una funzione = un compito specifico
- **Nomi descrittivi**: `calcola_totale()` è meglio di `calc()` o `f1()`

### Errori Comuni da Evitare
1. **Dimenticare return**: Se la funzione deve restituire un valore, usa `return`
2. **Modificare lista durante iterazione**: Crea una copia se devi rimuovere elementi
3. **KeyError nei dizionari**: Usa `.get(key, default)` invece di `[key]` se non sei sicuro
4. **Confronto stringhe case-sensitive**: Usa sempre `.lower()` o `.upper()` per confronti

### Comandi Utili
```python
# Liste
lista.append(elemento)
lista.remove(elemento)
lista.sort()
len(lista)

# Dizionari
dict[chiave] = valore
dict.get(chiave, default)
dict.keys()
dict.values()
dict.items()

# Stringhe
stringa.lower()
stringa.upper()
stringa.split()
stringa.strip()

# Operazioni
sum(lista)
max(lista)
min(lista)
sorted(lista)
```

---

## ✅ CHECKLIST COMPLETAMENTO

Prima di considerare l'esercizio completo, verifica:

- [ ] Il codice esegue senza errori
- [ ] Tutte le funzioni richieste sono implementate
- [ ] Le funzioni restituiscono i valori corretti (testa con esempi)
- [ ] Il codice è commentato dove necessario
- [ ] I nomi di variabili e funzioni sono descrittivi
- [ ] L'output è formattato in modo leggibile

---

**Buon lavoro! 🐍**
