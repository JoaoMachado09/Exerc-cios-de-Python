soma = 0
quantidade_notas = 0

while True:
    nota = float(input('Digite uma nota ou -1 para parar '))
    if nota == -1:
        break

    soma += nota
    quantidade_notas += 1


print(f"média da sala {soma//quantidade_notas}")