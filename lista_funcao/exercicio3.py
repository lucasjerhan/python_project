def reversoNumero(numero):
    reverso = int(str(numero)[::-1])
    return reverso

numero = int(input("Digite um número inteiro: "))

reverso = reversoNumero(numero)

print("O reverso do número é:", reverso)
