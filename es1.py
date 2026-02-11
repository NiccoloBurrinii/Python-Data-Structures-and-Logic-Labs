studente = [
    {"nome": "Mario Rossi", "voti": [28, 30, 27], "matricola": "12345", "corso": "Informatica"},
    {"nome": "Luigi Verdi", "voti": [25, 26, 24], "matricola": "12346", "corso": "Informatica"},
    {"nome": "Giulia Bianchi", "voti": [30, 30, 30], "matricola": "12347", "corso": "Matematica"},
]

def aggiungi_studente(lista, nome, matricola, corso):
    lista.append({"nome": nome, "matricola": matricola, "corso": corso})

def aggiungi_voto(lista, matricola, voto):
    for studente in lista:
        if studente["matricola"] == matricola:
            studente["voti"].append(voto)
            break

def calcola_media(lista, matricola):
    for studente in lista:
        if studente["matricola"] == matricola:
            return sum(studente["voti"]) / len(studente["voti"])
    return None

def studenti_per_corso(lista, corso):
    return [studente for studente in lista if studente.get("corso") == corso]

# Esempio di utilizzo
aggiungi_studente(studente, "Anna Neri", "12348", "Informatica")
aggiungi_voto(studente, "12345", 29)
media = calcola_media(studente, "12345")
print(f"Media voti di Mario Rossi: {media}")
studenti_informatica = studenti_per_corso(studente, "Informatica")
print("Studenti iscritti a Informatica:")
for s in studenti_informatica:
    print(s["nome"])