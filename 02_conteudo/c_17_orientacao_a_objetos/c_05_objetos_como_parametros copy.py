# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando
from datetime import datetime

#classes
class TV:

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Disney+'
        self.volume = 10
        self.canais_bloqueados = []

    @staticmethod
    def exibir_hora():
        print(datetime.now())

    def compartilhar_canal(self, tv_nova):
        tv_nova.canal = self.canal
        TV.exibir_hora()

    def alterar_canal(self, novo_canal: str):
        self.canal = novo_canal

#programa
tv_sala = TV(55)
tv_quarto = TV(70)

tv_quarto.compartilhar_canal(tv_sala)

print(f'Canal da sala: {tv_sala.canal}')
print(f'Canal do quarto: {tv_quarto.canal}')

tv_quarto.alterar_canal('Netflix')

print(f'Canal da sala mantido: {tv_sala.canal}')
print(f'Canal do quarto alterado: {tv_quarto.canal}')