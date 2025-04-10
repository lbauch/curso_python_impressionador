from datetime import datetime, timezone

class TV:

    def __init__(self, tamanho):
        # Para atributos internos, utiliza-se o underline na frente do atributo
        # Da mesma forma que os métodos. Com isso, define-se que estes atributos
        # somente podem ser alterados por métodos, públicos ou privados

        # ATENÇÃO - dois _ antes do nome indica que, dentro da classe, é 
        # possível utilizar o atributo. Porém, não é possível utilizar este atributo fora da classe
        self._ligada = False
        self._tamanho = tamanho
        self._canal = None
        self._volume = 10
        self._canais_bloqueados = []
        self.descicao = ""
        self.__frequencia_de_funcionamento = '500Hz'

    def _validar_canal(self):
        return self.canal == 'Desligar'

    def bloquear_canal(self, canal):
        self.canais_bloqueados.append(canal)

