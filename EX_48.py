cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cont += 1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))



#for c in range(1, 31):
#    if c % 3 == 0:
#        print(c, end=' ')


