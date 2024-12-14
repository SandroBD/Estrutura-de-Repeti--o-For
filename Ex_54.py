from datetime import date
data_atual = date.today().year
total_maior = 0
total_menor = 0
for c in range(1, 8):
    ano_nasc = int(input('informe o {}° ano de nascimento:'.format(c)))
    idade = data_atual - ano_nasc
    if idade >= 21:
            total_maior += 1
    else:
        total_menor += 1
print('Entre as datas informadas, {} ainda não atigiram a maior-idade e {} já são adultos'.format(total_menor, total_maior))












