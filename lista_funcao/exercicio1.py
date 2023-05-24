def somaImposto(taxaImposto, custo):
    custo += custo * (taxaImposto / 100)
    return custo

taxa = float(input("Digite a taxa de imposto sobre vendas (%): "))
preco = float(input("Digite o custo do item: "))

preco_total = somaImposto(taxa, preco)

print("O custo total com imposto é:", preco_total)
