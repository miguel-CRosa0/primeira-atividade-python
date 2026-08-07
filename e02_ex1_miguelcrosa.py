soma = 0

for i in range(5):
    valor = float(input("numero\n--> "))
    soma += valor
    

media = soma / 5

print(f"A soma dos numeros escolhidos é: {soma:.2f}")
print(f"A média dos numeros é: {media:.2f}")