
## Conversor pesos a dolares

pesos = input("¿cuantos pesos colombianos tienes?")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")

## Conversor dolares a pesos
dolares = input("¿cuantos dolares tienes?")
dolares = float(dolares)
valor_dolar = 3875
pesos = dolares * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")

