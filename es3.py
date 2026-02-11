import string


def genera_password(lunghezza, maiuscole=True, numeri=True, simboli=True):
    import random
    import string

    caratteri = string.ascii_lowercase
    if maiuscole:
        caratteri += string.ascii_uppercase
    if numeri:
        caratteri += string.digits
    if simboli:
        caratteri += string.punctuation

    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password

def verifica_complessita(password):
    complessita = {"lunghezza_ok": False,
                    "maiuscole_ok": False,
                      "numeri_ok": False,
                        "simboli_ok": False,
                          "minuscole_ok": False
                          }

    if len(password) >= 8:
        complessita["lunghezza_ok"] = True

    if any(c.isupper() for c in password):
        complessita["maiuscole_ok"] = True

    if any(c.isdigit() for c in password):
        complessita["numeri_ok"] = True

    if any(c in string.punctuation for c in password):
        complessita["simboli_ok"] = True

    if any(c.islower() for c in password):
        complessita["minuscole_ok"] = True

    return complessita
      
def output_complessita(complessita):
    for criterio, soddisfatto in complessita.items():
        stato = "✓" if soddisfatto else "✗"
        print(f"{criterio}: {stato}")
        
# Richiesta e validazione dell'input (ripete finché non riceve un intero positivo)
while True:
    valore = input("Inserisci la lunghezza desiderata per la password: ")
    try:
        input_lunghezza = int(valore)
        if input_lunghezza <= 0:
            print("Inserire un numero intero positivo.")
            continue
        break
    except ValueError:
        print("Valore non valido. Inserisci un numero intero.")


password= genera_password(input_lunghezza)

print("Password generata:", password)
output_complessita(verifica_complessita(password))
