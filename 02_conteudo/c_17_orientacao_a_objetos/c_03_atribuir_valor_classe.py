# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:

    # Desta forma, indica que todas as televisões irão possuir o atributo cor.
    # Porém, todos os objetos terão o mesmo valor
    cor = 'preta'

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV(55)
tv_quarto = TV(70)

# É possível fazer desta forma. Entretanto, não é nada recomendado.
tv_quarto.cor = 'branca'

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print(tv_sala.cor)
print(tv_quarto.cor)

