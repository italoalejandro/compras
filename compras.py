'''Crie uma lista com os itens e o valor para uma compra de um supermercado.'''

itens = {

"maçã": 5,
"laranja": 7,
"uva": 3,
"leite": 4,
}

print("-----------------")

'''Mostre a lista e o valor total da compra.'''
# Exibição da lista e cálculo do valor total
print("-----------------")
print("Lista de compras:")
for item, valor in itens.items():
    print(f"{item}: R${valor:.2f}")

# Cálculo do valor total
valor_total = sum(itens.values())
print("-----------------")
print(f"Valor total da compra: R${valor_total:.2f}")
print("-----------------")
