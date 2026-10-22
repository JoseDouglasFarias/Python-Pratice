#receber lista de valores.
#retornar total de despesas, quantidade de valores maior que 30 e o maior dos valores.

valores = [10, 20, 30, 40, 50]

def analisar_despesas(valores):
    #caso a lista esteja vazia.
    if valores == []:
        return 0,0,None

    
    total_despesas = 0
    quantidade_maior_30 = 0
    maior_valor = valores[0]

    for i in valores:
        #soma de todos os valores
        total_despesas += i

        #quantidade de valores maior que 30
        if i > 30:
            quantidade_maior_30 += 1

        #maior valor
        if i > maior_valor:
            maior_valor = i

    return total_despesas, quantidade_maior_30, maior_valor

#fatorando a função analisar_despesas para receber a lista de valores e retornar os resultados.
total,quantidade_maior_30,maiorvalor = analisar_despesas(valores)
print("Total de despesas:", total)
print("Quantidade de valores maior que 30:", quantidade_maior_30)
print("Maior valor:", maiorvalor)