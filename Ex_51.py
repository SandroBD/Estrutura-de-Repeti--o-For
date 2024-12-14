a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA:'))
decimo = a1 + ( 10 - 1 ) * r
for c in range(a1, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')


