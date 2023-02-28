"""
1-
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print(n1 + n2)
=================================================================
2-
medida_metros = int(input('Digite a medida em metros: '))
medida_milimetros = medida_metros * 1000
print(medida_milimetros)
=================================================================
3-
dia = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

dia_seg = dia * 86400
horas_seg = horas * 3600
minutos_seg = minutos * 60

total = dia_seg + horas_seg + minutos_seg + segundos

print(total)
=================================================================
4-
salario = int(input('Digite o valor do salário: R$ '))
porcentagem = int(input('Digite o valor da procentagem: % '))
porcentagem_salario = salario * (porcentagem / 100)
salario_novo = salario + porcentagem_salario
print(salario_novo)
=================================================================
5-
mercadoria = int(input('Digite o valor da mercadoria: R$ '))
porcentagem = int(input('Digite o valor do desconto: % '))
porcentagem_mercadoria = mercadoria * (porcentagem / 100)
desconto = mercadoria - porcentagem_mercadoria
print(desconto)
=================================================================
TWP115-
velocidade = int(input('Informe a velocidade: '))

if velocidade > 110:
    multa = (velocidade - 110) * 5
    print(f'Você foi multado em R$ {multa}')
else:
    print('Velocidade normal')
=================================================================
TWP120-
minutos = int(input('Informe a minutagem: '))
if minutos < 200:
    valor = minutos * 0.2
elif minutos > 400:
    valor = minutos * 0.15
else:
    valor = minutos * 0.18

print(f'R${valor: .2f}')


"""



