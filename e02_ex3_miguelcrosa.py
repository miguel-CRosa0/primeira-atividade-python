matriz = []
soma_total = 0

maior_valor = 0
pos_maior_linha = 0
pos_maior_coluna = 0


for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
        soma_total += valor
        
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            pos_maior_linha = i
            pos_maior_coluna = j
            
    matriz.append(linha)

print("\n" + "---------------------" + "\n")

print("Matriz digitada:")
for linha in matriz:
    print(linha)

print("\n" + "---------------------" + "\n")

print("--- SOMA DE CADA LINHA ---")
for l in range(3):
    soma_linha = sum(matriz[l])
    print(f"Soma da Linha {l}: {soma_linha}")

print("\n" + "---------------------" + "\n")

print("--- SOMA DE CADA COLUNA ---")
for c in range(3):
    soma_coluna = 0
    for l in range(3):
        soma_coluna += matriz[l][c]
    print(f"Soma da Coluna {c}: {soma_coluna}")

print("\n" + "---------------------" + "\n")

print("--- RESULTADOS FINAIS ---")
print(f"A soma total de todos os elementos da matriz é: {soma_total}")
print(f"O maior valor encontrado foi {maior_valor}, localizado na Linha {pos_maior_linha}, Coluna {pos_maior_coluna}.")