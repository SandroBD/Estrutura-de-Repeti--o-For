soma_idade = 0
total_pessoas = 0
h_maisvelho = 0
nhmaisvelho = ''
m_menosvinte = 0
for c in range(1, 5):
    print('--> Dados da {}° pessoa'.format(c))
    nome: str = str(input('Informe o nome: ')).strip().title()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: ')).strip().title()
    soma_idade += idade
    total_pessoas += 1
    if c == 1 and sexo == 'Masculino':
        h_maisvelho = idade
    elif sexo == 'Masculino' and idade > h_maisvelho:
        h_maisvelho = idade
        nhmaisvelho = nome
    elif sexo == 'Feminino' and idade < 20:
        m_menosvinte += 1
media = soma_idade / total_pessoas
print('Média das idades do grupo: {:.2f} \nNome do homem mais velho: {}, {} anos\n{} mulheres têm menos de 20 anos'.format(media, nhmaisvelho, h_maisvelho, m_menosvinte ))




