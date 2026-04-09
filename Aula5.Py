texto = input()

contador = 0
for letra in texto:
    if letra == 'a' or letra == 'o':
        contador += 1

print(contador)
