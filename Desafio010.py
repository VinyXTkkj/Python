real = float(input('Quantos Dinheiro você tem na Carteira? R$'))
dolar = real / 4.80
euro = real/ 5.24
euro2 = real*5.24
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com €{:.2f} você tem R${:.2f}'.format(euro2, real))
