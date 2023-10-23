n = input()
m = input()
z = input()
if n == 'vertebrado':
    if m == 'ave':
        if z == 'carnivoro':
            print('aguia')
        elif z == 'onivoro':
            print('pomba')
    elif m == 'mamifero':
        if z == 'onivoro':
            print('homem')
        elif z == 'herbivoro':
            print('vaca')
elif n == 'invertebrado':
    if m == 'inseto':
        if z == 'hematofago':
            print('pulga')
        elif z == 'herbivoro':
            print('lagarta')
    elif m == 'anelideo':
        if z == 'hematofago':
            print('sanguessuga')
        elif z == 'onivoro':
            print('minhoca')