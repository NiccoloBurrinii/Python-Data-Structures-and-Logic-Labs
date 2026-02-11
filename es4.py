def aggiungi_prodotto(inventario, id, nome, categoria, prezzo, quantita):
	# Crea un dizionario che rappresenta un prodotto e lo aggiunge
	# all'elenco `inventario` (modifica in-place).
	# Parametri:
	# - inventario: lista di dizionari (ogni dizionario è un prodotto)
	# - id, nome, categoria, prezzo, quantita: valori del prodotto
	prodotto = {"id": id, "nome": nome, "categoria": categoria, "prezzo": prezzo, "quantita": quantita}
	inventario.append(prodotto)


def rimuovi_prodotto(inventario, id):
	# Rimuove il prodotto con l'id specificato dall'inventario.
	# Scorriamo con `enumerate` per ottenere l'indice da usare con `pop`.
	# Se il prodotto viene trovato, viene rimosso e restituito; altrimenti None.
	for i, p in enumerate(inventario):
		if p.get("id") == id:
			return inventario.pop(i)
	return None


def cerca_prodotto(inventario, nome):
	# Ricerca case-insensitive: restituisce tutti i prodotti il cui campo
	# `nome` contiene la stringa `nome` passata (ignorando maiuscole/minuscole).
	nome_lower = nome.lower()
	return [p for p in inventario if nome_lower in p.get("nome", "").lower()]


def prodotti_per_categoria(inventario, categoria):
	# Filtra e restituisce la lista dei prodotti appartenenti alla categoria.
	return [p for p in inventario if p.get("categoria", "") == categoria]


def valore_totale_inventario(inventario):
	# Calcola il valore totale dell'inventario: somma di (prezzo * quantita)
	# per ogni prodotto. Usa `get` con valori di default per sicurezza.
	return sum(p.get("prezzo", 0) * p.get("quantita", 0) for p in inventario)


def prodotti_sotto_scorta(inventario, soglia=10):
	# Restituisce i prodotti la cui quantità è inferiore alla `soglia`.
	# `soglia` ha valore predefinito 10 ma può essere cambiata.
	return [p for p in inventario if p.get("quantita", 0) < soglia]


if __name__ == "__main__":
	# Blocco principale: codice eseguito solo se si lancia direttamente il file
	# Qui definiamo un inventario di esempio composto da dizionari.
	inventario = [
		{"id": 1, "nome": "Laptop Dell", "categoria": "Elettronica", "prezzo": 800, "quantita": 5},
		{"id": 2, "nome": "Mouse Logitech", "categoria": "Elettronica", "prezzo": 25, "quantita": 50},
		{"id": 3, "nome": "Sedia Ergonomica", "categoria": "Arredamento", "prezzo": 200, "quantita": 8},
		{"id": 4, "nome": "Scrivania", "categoria": "Arredamento", "prezzo": 350, "quantita": 3}
	]

	# 1) Calcolo del valore totale dell'inventario
	# chiamiamo `valore_totale_inventario` e stampiamo formattando con due decimali
	valore = valore_totale_inventario(inventario)
	print(f"Valore totale inventario: €{valore:,.2f}\n")

	# 2) Elenco dei prodotti sotto scorta (quantita < soglia)
	# Utilizziamo la funzione `prodotti_sotto_scorta` con soglia 10
	sotto = prodotti_sotto_scorta(inventario, soglia=10)
	print("Prodotti sotto scorta (< 10):")
	# Per ogni prodotto sotto scorta stampiamo il nome e la quantità
	for p in sotto:
		print(f"- {p['nome']}: {p['quantita']} unit\u00e0")
	print()

	# 3) Esempio di ricerca: cerchiamo prodotti che contengono 'dell' nel nome
	term = "dell"
	trovati = cerca_prodotto(inventario, term)
	print(f"Ricerca \"{term}\":")
	# Stampiamo nome, categoria, prezzo formattato e quantità per ogni risultato
	for p in trovati:
		print(f"- {p['nome']} ({p['categoria']}): €{p['prezzo']:,.2f} x {p['quantita']}")
	print()

	# 4) Esempio: prodotti per categoria
	cat = "Elettronica"
	per_cat = prodotti_per_categoria(inventario, cat)
	print(f"Categoria {cat}:")
	# Stampiamo ogni prodotto della categoria con prezzo e quantità
	for p in per_cat:
		print(f"- {p['nome']}: €{p['prezzo']:,.2f} x {p['quantita']}")

#