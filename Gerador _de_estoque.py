import random

qtd = 10
estoque_vetor = []
estoque_min_vetor = []
estoque_max_vetor = []
preco_compra_vetor = []
preco_venda_vetor = []
icms_vetor = []
ipi_vetor = []
vetor_lucro = []
nomes_produtos = ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", "Produto F", "Produto G", "Produto H" ,"Produto I" ,"Produto J"]  # Substitua com os nomes reais dos produtos

for i in range(qtd):
    produto = i
    codigo = random.randint(1, 100)
    estoque = random.randint(1, 100)
    estoque_vetor.append(estoque)
    
    estoque_min = random.randint(1, 100)
    estoque_max = random.randint(1, 100)

    while estoque_min >= estoque_max:               #VERIFICAÇÃO EM LOOP PARA NAO TER ESTOQUE MINIMO MAIOR QUE O MAXIMO!!!
        estoque_min = random.randint(1, 100)

    preco_compra = float(random.randint(1, 1000))
    preco_compra_vetor.append(preco_compra)

    preco_venda = float(random.randint(1, 1000))    #VERIFICAÇÃO EM LOOP PARA NAO TER PRECO DE COMPRA MAIOR QUE VENDA!!!
    while preco_venda <= preco_compra:
        preco_venda = float(random.randint(1, 1000))
    preco_venda_vetor.append(preco_venda)
    
    icms = float(random.randint(1, 17))
    icms_vetor.append(icms)
    
    ipi = float(random.randint(1, 50))
    ipi_vetor.append(ipi)
    
    vetor_lucro.append(preco_venda - preco_compra)

    print("==============================")
    print(" Produto:", nomes_produtos[i], "\n Codigo:", codigo, "\n Estoque:", estoque, "\n Estoque Minimo:",
          estoque_min, "\n Estoque Maximo:", estoque_max, "\n Preco de Compra:", preco_compra, "\n Preco de Venda:",
          preco_venda, "\n ICMS:", icms, "%", "\n IPI:", ipi, "%")
    print("==============================")

indice_maior_estoque = estoque_vetor.index(max(estoque_vetor))
indice_menor_estoque = estoque_vetor.index(min(estoque_vetor))
indice_maior_preco_compra = preco_compra_vetor.index(max(preco_compra_vetor))
indice_menor_preco_compra = preco_compra_vetor.index(min(preco_compra_vetor))
indice_maior_icms = icms_vetor.index(max(icms_vetor))
indice_menor_icms = icms_vetor.index(min(icms_vetor))
indice_maior_lucro = vetor_lucro.index(max(vetor_lucro))
indice_menor_lucro = vetor_lucro.index(min(vetor_lucro))

print('Produto com maior estoque:', max(estoque_vetor), ":", nomes_produtos[indice_maior_estoque])
print('Produto com menor estoque:', min(estoque_vetor), ":", nomes_produtos[indice_menor_estoque])
print('Produto com maior preco de compra:', max(preco_compra_vetor), ":", nomes_produtos[indice_maior_preco_compra])
print('Produto com menor preco de compra:', min(preco_compra_vetor), ":", nomes_produtos[indice_menor_preco_compra])
print('Produto com maior ICMS:', max(icms_vetor), "%", ":", nomes_produtos[indice_maior_icms])
print('Produto com menor ICMS:', min(icms_vetor), "%", ":", nomes_produtos[indice_menor_icms])
print('Produto com maior lucro:', max(vetor_lucro), ":", nomes_produtos[indice_maior_lucro])
print('Produto com menor lucro:', min(vetor_lucro), ":", nomes_produtos[indice_menor_lucro])