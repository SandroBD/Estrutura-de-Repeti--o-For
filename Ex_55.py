maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input('Informe o {}° peso: Kg'.format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print('Menor peso: {}Kg \nMaior peso: {}Kg'.format(menor_peso, maior_peso))
