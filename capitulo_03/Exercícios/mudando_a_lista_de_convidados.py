lista_convidados = ['Ana', 'Maria', 'João']

print(f"{lista_convidados[0]}, você quer jantar?")
print(f"{lista_convidados[1]}, você quer jantar?")
print(f"{lista_convidados[2]}, você quer jantar?")

faltante = lista_convidados.pop(2)

print(f"{faltante} não poderá ir ao jantar")
lista_convidados.insert(2, "José")

print(f"{lista_convidados[0]}, você quer jantar?")
print(f"{lista_convidados[1]}, você quer jantar?")
print(f"{lista_convidados[2]}, você quer jantar?")