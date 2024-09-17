# Função que garante que os números negativos não fazem parte da sequência de Fibonacci
def pertence_fibonacci(numero):
    if numero < 0:
        return False
    termo1 = 0
    termo2 = 1
    
    if numero == termo1 or numero == termo2:
        return True

    while True:
        termo3 = termo1 + termo2
        if termo3 == numero:
            return True
        elif termo3 > numero:
            return False
        termo1 = termo2
        termo2 = termo3

numero = int(input('Digite um número inteiro para verificar se faz parte da sequência de Fibonacci:'))

if pertence_fibonacci(numero):
    print(f'{numero} faz parte da sequência de Fibonacci.')
else:
    print(f'{numero} não faz parte da sequência de fibonacci.')