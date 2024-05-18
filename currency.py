

pesos = int(input("How many pesos do you have?: "))

soles = int(input("How many soles do you have?: "))

reais = int(input("How many reais do you have?: "))

# Conversion rates

pesos_to_dollars = 0.051
soles_to_dollars = 0.29
reais_to_dollars = 0.18

# Conversion of currency to dollars

dollars = (pesos * pesos_to_dollars) + (soles * soles_to_dollars) + (reais * reais_to_dollars)

print(f"You have {dollars} dollars")