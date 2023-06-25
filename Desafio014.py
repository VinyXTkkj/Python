# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. #
# Write a program that converts a temperature typed into degrees Celsius and converts to degrees Fahrenheit #

temp = float(input('Informa a temperatura em °C: '))
c = 32 + (temp*1.8)
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(temp, c))