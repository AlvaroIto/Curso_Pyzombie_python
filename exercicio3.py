"""
1-
nota = int(input('Digite a nota: '))
while nota < 0 or nota > 10:
    print('Valor Inválido!')
    break
else:
    print(f'Nota: {nota}')
=================================================================
2-
nome = str(input('Digite seu nome: '))
senha = str(input('Digite sua senha: '))

while senha == nome:
    print('Erro')
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: '))

else:
    print(f'Nome: {nome}')
    print(f'Senha: {senha}')
=================================================================
3-
A = 80000
B = 200000
anos = 0

while A < B:
    A = A * 0.03 + A
    B = B * 0.015 + B
    anos = anos + 1

print(anos)
=================================================================
4-

"""




