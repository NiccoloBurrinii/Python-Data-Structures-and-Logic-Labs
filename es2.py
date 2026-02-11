import re

testo = """Python è un linguaggio di programmazione potente e facile da imparare.
Ha strutture dati efficienti e un approccio semplice ma efficace alla programmazione orientata agli oggetti."""


def conta_parole (testo):
    testo = testo.lower()
    testo = re.sub(r'[^\w\s]', '', testo)
    numParole = len(testo.split())
    return numParole

def conta_caratteri (testo):
    testo=testo.replace(" ", "")   
    numCaratteri = len(testo)
    return numCaratteri

def parola_piu_lunga (testo):
    parole = testo.split()
    parola_lunga = max(parole, key=len)
    count = 0

    for parola in parole:
        if parola_lunga == parola:
            count+=1

    return parola_lunga, count

def frequenza_parole (testo):
    parole = testo.split()
    frequenza = {}

    for parola in parole:
        if parola in frequenza:
            frequenza[parola] += 1
        else:
            frequenza[parola] = 1

    return frequenza

def output_frequenza(frequenza):
    for parola, count in frequenza.items():
        print(f"{parola}: {count}")

def parola_piu_frequente (testo):
    parole = testo.split()
    frequenza = {}

    for parola in parole:
        if parola in frequenza:
            frequenza[parola] += 1
        else:
            frequenza[parola] = 1

    max_count = max(frequenza.values())
    parole_frequenti = [parola for parola, count in frequenza.items() if count == max_count]

    return parole_frequenti, max_count

print(testo)

print("Il numero di parole è:", conta_parole(testo))
print("Il numero di caratteri è:", conta_caratteri(testo))

output_frequenza(frequenza_parole(testo))
parola, count = parola_piu_lunga(testo)
print(f"La parola più lunga è: {parola}, N volte che appare: {count}")
print("La parola più frequente è:", parola_piu_frequente(testo))