notas = []
media = 6
posicao = 0
notasMedia = 0

for i in range(6):
    nota = float(input(f"Qual a {i+1} nota?\n--> "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Maior: ", max(notas))
print("Menor: ", min(notas))
print(f"Media: {media:.2f} ")

for valor in notas:
    posicao += 1
    if(valor > 6):
        print(f"Nota {valor}, da posição {posicao} está acima da media.")
        notasMedia += 1
    else:
        print(f"Nota {valor}, da posição {posicao} está abaixo da média.")
        
print(f"Teve um total de {notasMedia} acima da média")