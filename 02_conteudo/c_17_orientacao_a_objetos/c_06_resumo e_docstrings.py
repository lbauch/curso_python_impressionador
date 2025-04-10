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
    """

    IMPORTANTE - VER PEP 257 - PADRÃO DE DOCSTRING

    Cria um objeto fictício de tv, apenas para mostrar funcionamento dos métodos
    internos, estáticos, públicos e que recebem a própria classe como parâmetro

    Args:
        ligada (bool): Status da tv
        tamanho (float): tamanho em polegadas da tv
        canal (str): 
        volume (int): volume atual da tv
        canais_bloqueados (Array): Lista com todos os canais bloqueados
    """

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Disney+'
        self.volume = 10
        self.canais_bloqueados = []

    @staticmethod
    def exibir_hora():
        """
        Demonstração de método estátoco, apenas imprime a hora atual e pode ser
        utilizado fora da classe

        Exibe a hora atual do sistema
        """
        print(datetime.now())

    def _validar_canal(self, canal: str) -> bool:
        """
        Demonstração de método interno: underline na frente, mostrando que é privado.
        Seta indica o tipo de retorno

        Verifica se o canal é válido.
        
        Args:
            canal (str): Canal que se deseja validar se está entre os permitidos
        """
        return canal == 'Disney+' or canal == 'Netflix'


    def compartilhar_canal(self, tv_nova : 'TV'):
        """
        Demonstração de método público que recebe como parâmetro a própria classe

        Compartilha o canal da tv objeto com a tv passada como parâmetro
        
        Args
            tv_nova (TV): tv que irá receber o canal da tv atual
        """
        tv_nova.canal = self.canal
        TV.exibir_hora()

    def alterar_canal(self, novo_canal: str):
        if self._validar_canal(novo_canal):
            self.canal = novo_canal
        else:
            print('Canal inválido')

#programa
tv_sala = TV(55)
tv_quarto = TV(70)

tv_quarto.compartilhar_canal(tv_sala)

print(f'Canal da sala: {tv_sala.canal}')
print(f'Canal do quarto: {tv_quarto.canal}')

tv_quarto.alterar_canal('NETEFLICS')

tv_quarto.alterar_canal('Netflix')
print(f'Canal da sala mantido: {tv_sala.canal}')
print(f'Canal do quarto alterado: {tv_quarto.canal}')

# *********** IMPORTANTE ***********
# Visualizar a doc da classe:
# help(nome_da_classe)