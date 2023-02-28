"""
1-
l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Não pode ser um triangulo')
elif l1 == l2 == l3:
    print('Equilátero')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Isósceles')
else:
    print('Escaleno')
=================================================================
2-
=================================================================
3-
peso = float(input('Digite o peso do peixe: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print(f'Multa de R$ {multa: .2f}')
print(f'Excesso {excesso: .2f}')
=================================================================
4-
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 > n2 and n1 > n3:
    print('Número 1 é maior')
elif n2 > n1 and n2 > n3:
    print('Número 2 é maior')
elif n3 > n1 and n3 > n2:
    print('Número 3 é maior')
else:
    print('Números iguais')
=================================================================
TWP160-
y = int(input('Digite um número: '))
x = 1
while x <= y:
    print(x)
    x = x + 1
=================================================================

"""
 




