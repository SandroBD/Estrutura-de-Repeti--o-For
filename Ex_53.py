frase = str(input('Digite um frase: ')).strip().upper()
palavras =  frase.split() # split vai dividir a frase em uma lista formada por cada palavra da frase
junto = ''.join(palavras) # vai juntar todas as palavras da lista sem deixar espaço entre elas
inverso = junto[::-1] # fatiamento
#inverso = '' # uma variável vazia para receber string
#for letra in range(len(junto) - 1, -1, -1): # len(junto) vai me mostrar o comprimento da frase
#    inverso += junto[letra]
if junto == inverso:
    print( 'A frase {} e seu inverso {} formam um palíndromo'.format(junto, inverso))
else:
    print('A frase {} e seu inverso {} Não formam  um palíndromo'.format(junto,inverso))






