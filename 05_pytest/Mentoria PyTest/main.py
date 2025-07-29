# Pytest, o que é
    # Em códigos pequenos não parece ter aplicação, mas quando você cria
    # sistemas grandes, faz sentido
# Não é uma ferramenta ultra obrigatória o tempo todo pra todo código
# Funcionamento -> instalar e rodar testes
    # sem nada
    # formato de teste (nome nos arquivos e nas funções)
        # ele não printa a função, ele roda e vê se deu algum erro.
            # . se der certo
            # F se der errado
            # E onde deu alguma coisa errada
# mostrar com a função real, importando ela e com números ok
# usar o assert
# crar a função calcular o faturamento. Mostrar que não dá merda nela
# então você testou o calcular lucro, ta ok, testou o calcular faturamento, ta ok, bora seguir
# testar colocando o calcular faturamento dentro do calcular lucro, vai dar merda
    # vantagem, você vai criando meio que vários pontos de teste ao longo do seu código que podem ser sempre executados
    # testes de sanidade -> parece bobo, parece idiota, mas é pra ser isso mesmo
    # agora, quanto maior fica o seu código, maiores ficam seus testes
# rodar só funções marcadas de algo específico (@pytest.mark.marcador)
    # lembrar de criar o pytest.ini
# separar em vários arquivos de teste
# fixtures -> criar uma função que calcula o custo



### pip install pytest

def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro

def calcular_faturamento():
    vendas = [10, 20, 30, 40]
    faturamento = sum(vendas)
    # return f"O faturamento é de {faturamento}"
    return faturamento

def calcular_custo(cotacao_dolar):
    # custos fixos em dolar
    custo = 50 * cotacao_dolar
    return custo
