p1 = float(input('Largura da parede: '))
p2 = float(input('Altura da parede: '))
a = p1*p2
l = a/2
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(p1, p2, a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(l))
