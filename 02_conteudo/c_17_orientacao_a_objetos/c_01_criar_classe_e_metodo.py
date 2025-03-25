# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# criar uma classe:
# class Nome_Classe:
#
# Dentro de uma classe, as functions são métodos
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
# Sempre que um objeto for criado, oque está dentro de __init__ será executado.
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:

    def __init__(self):
        # Ao inicializar a classe, cria uma variável para cada elemento após o self e atribui o valor padrão.
        # Neste caso, para cada objeto criado, cria e define o valor de cor, ligada, tamanho, canal e volume.
        # Sempre que se quer atribuir um valor para a classe, dentro do método é necessário passar o self.
        # Neste caso, definição é uma variável criada somente interna ao método e não pode ser acessada por fora.
        definicao = '4K'
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self):
        if self.canal == "Netflix":
            self.canal = "Disney+"
        else:
            self.canal = "Netflix"


#programa
tv_sala = TV()
tv_quarto = TV()

# NÃO DEVE SER UTILIZADO - FEITO SOMENTE PARA EXEMPLO
# Para fazer isto da forma correta, é necessário criar métodos
tv_sala.cor = 'branca'

tv_sala.mudar_canal()
print(tv_sala.canal)
tv_sala.mudar_canal()
print(tv_sala.canal)


tv_quarto.mudar_canal()
print(tv_sala.cor)
print(tv_sala.canal)
print(tv_quarto.canal)

