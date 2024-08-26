import random

chars = '!?¿*_1234567890-#¡qwertuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM@'
password = ''

lengthPW = int(input('¿Qué lingitud quieres que tenga la contraseña? :)'))

for _ in range(lengthPW):

    password += random.choice(chars)

print(password)