def contarDigitos(frase):
    quantidade_digitos = sum(char.isdigit() for char in frase)
    return quantidade_digitos

frase = input("Digite uma frase: ")

quantidade_digitos = contarDigitos(frase)

print("A quantidade de dígitos na frase é:", quantidade_digitos)
