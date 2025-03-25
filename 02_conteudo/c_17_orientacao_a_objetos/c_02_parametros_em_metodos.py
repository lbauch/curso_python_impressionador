# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

# classes
class TV:

    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligada = False
        # self.tamanho - atribui o valor ao atributo tamanho do objeto criado; tamanho refere-se ao parâmetro passado
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print('canal alterado para {}'.format(novo_canal))
    # Recomendado: fazer como abaixo, mantendo o mesmo nome para o parâmetro e atributo
    # def mudar_canal(self, canal):
    #     self.canal = canal


# programa
# Ao instanciar, somente passa os parâmetros diferente de self
tv_sala = TV(55)
tv_quarto = TV(70)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

