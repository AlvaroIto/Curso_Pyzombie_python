"""
IF ELSE

Considere a empresa de telefonia Tchau.
Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto. Entre 200 e 400 minutos, o preço é R$ 0,18.
Acima de 400 minutos o preço pro minuto é R$ 0,15. Calcule a sua conta de telefone


minutos = int(input('Minutos: '))

if minutos < 200:
    preco = 0.2

else:
    if minutos <= 400:
        preco = 0.18

    else:
        preco = 0.15

print(f'R$ {preco*minutos:.2f}')

=================================================================
ELIF

Modifique o programa da empresa Tchau para uma promoção onde a tarifa é de R$ 0,08
quando você utiliza mais que 800 minutos


minutos = int(input('Minutos: '))
if minutos < 200:
    preco = 0.2

elif minutos <= 400:
    preco = 0.18

elif minutos <= 800:
    preco = 0.15

else:
    preco = 0.08

print(f'R$ {preco*minutos:.2f}')

"""
