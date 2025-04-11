from datetime import datetime, timezone

class TV:

    def __init__(self, tamanho):
        # Para atributos internos, utiliza-se o underline na frente do atributo
        # Da mesma forma que os métodos. Com isso, define-se que estes atributos
        # somente podem ser alterados por métodos, públicos ou privados

        # ATENÇÃO - dois _ antes do nome indica que, dentro da classe, é 
        # possível utilizar o atributo. Porém, não é possível utilizar este atributo fora da classe

        # OBSERVAÇÃO IMPORTANTE: Para atributos que não precisam de validação para serem criados
        # ou podem ser acessados e alterados de forma direta, não se recomenda o underline
        # Parta estes casos recomenda-se utilizar o atributo puro.
        # Exemplo: Tv1 = TV(55)
        # print(Tv1.tamanho)
        # Tv1.descricao = "Televisão 1"
        self._ligada = False
        self.tamanho = tamanho
        self._canal = None
        self._volume = 10
        self._canais_bloqueados = []
        self.descicao = ""
        self.__frequencia_de_funcionamento = '500Hz'

    def _validar_canal(self):
        return self.canal == 'Desligar'

    def bloquear_canal(self, canal):
        self.canais_bloqueados.append(canal)

Tv1 = TV(55)

# UTILIZA O MÉTODO INTERNO __dict__ PARA MOSTRAR TODOS OS ATRIBUTOS
print(Tv1.__dict__)

# {'_ligada': False, 'tamanho': 55, '_canal': None, '_volume': 10, '_canais_bloqueados': [], 'descicao': '', '_TV__frequencia_de_funcionamento': '500Hz'}