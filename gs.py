import random
import string

tamanho = int(input("O tamanho de senha necessário é: "))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+_,.;:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))