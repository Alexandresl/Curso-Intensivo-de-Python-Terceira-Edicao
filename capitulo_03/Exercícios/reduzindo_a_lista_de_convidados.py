lista_convidados = ['Ana', 'Maria', 'João']

print(f"{lista_convidados[0]}, você quer jantar?")
print(f"{lista_convidados[1]}, você quer jantar?")
print(f"{lista_convidados[2]}, você quer jantar?")

print("\nEncontrei uma mesa maior!")

lista_convidados.insert(0, "Luíza")
lista_convidados.insert(2, "Juliano")
lista_convidados.append("Gabriela")

print(f"\n{lista_convidados[0]} quer jantar?")
print(f"{lista_convidados[1]} quer jantar?")
print(f"{lista_convidados[2]} quer jantar?")
print(f"{lista_convidados[3]} quer jantar?")
print(f"{lista_convidados[4]} quer jantar?")
print(f"{lista_convidados[5]} quer jantar?")

print(f"\nSó posso convidar duas pessoas para o jantar!")

convidado_removido = lista_convidados.pop()
print(f"\n{convidado_removido}, lamento mas terei que cancelar o jantar.")
convidado_removido = lista_convidados.pop()
print(f"{convidado_removido}, lamento mas terei que cancelar o jantar.")
convidado_removido = lista_convidados.pop()
print(f"{convidado_removido}, lamento mas terei que cancelar o jantar.")
convidado_removido = lista_convidados.pop()
print(f"{convidado_removido}, lamento mas terei que cancelar o jantar.")

print(f"\n{lista_convidados[0]}, você ainda está convidado para o jantar")
print(f"{lista_convidados[1]}, você ainda está convidado para o jantar")

del lista_convidados[0]
del lista_convidados[0]

print(lista_convidados)
