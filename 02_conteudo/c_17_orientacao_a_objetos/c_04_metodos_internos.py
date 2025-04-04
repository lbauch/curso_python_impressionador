# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando
from datetime import datetime, timezone

#classes
class TV:

    # Desta forma, indica que todas as televisões irão possuir o atributo cor.
    # Porém, todos os objetos terão o mesmo valor
    cor = 'preta'

    # Métodos estáticos NÃO utilizam atributos da classe.
    # Por convenção, utiliza-se o decorator @staticmethod para informar que não usa atributos internos
    @staticmethod
    def _hora_agora():
        # timezone.utc - transforma a hora atual para o timezone 0
        agora = datetime.now(timezone.utc)
        # Define a hora formatada no padrão internacional, ISO 8601
        return agora.isoformat().replace('+00:00', 'Z')

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = None
        self.volume = 10
        self.canais_bloqueados = []

    # Método apenas para mostrar o uso do underline
    # O underline antes representa método privado
    def _validar_canal(self):
        return self.canal == 'Desligar'
        
    def mudar_canal_ou_desligar(self, novo_canal):
        # Ao chamar um método interno, é necessário utilizar o self antes do método
        if self._validar_canal():
            self.canal = None
            self.ligada = False
        else:
            self.canal = novo_canal

    def bloquear_canal(self, canal):
        self.canais_bloqueados.append(canal)

    def programar_ligar(self):
        agora = self._hora_agora()
        if agora.hour == 18 and agora.minutes == 0:
            self.ligada = True

#programa
tv_sala = TV(55)
tv_quarto = TV(70)

# É possível fazer desta forma. Entretanto, não é nada recomendado.
tv_quarto.cor = 'branca'

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print(tv_sala.cor)
print(tv_quarto.cor)

