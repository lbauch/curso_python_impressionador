from random import randint

# Classe principal
class Agencia:

  def __init__(self, telefone, cnpj, numero):
    self.telefone = telefone
    self.cnpj = cnpj
    self.numero = numero
    self.clientes = []
    self.caixa = 0
    self.emprestimos = []

  def verificar_caixa(self):
    if self.caixa < 1000000:
      print('Caixa abaixo do nível recomendado. Caixa atual: {}'.format(self.caixa))
    else:
      print('O valor de caixa está ok. Caixa atual: {}'.format(self.caixa))

  def emprestar_dinheiro(self, valor, cpf, juros):
    if self.caixa > valor:
      self.emprestimos.append((valor, cpf, juros))
    else:
      print('Empréstimo não é pssível. Dinheiro indisponível em caixa')

  def adicionar_cliente(self, nome, cpf, patrimonio):
    self.clientes.append((nome, cpf, patrimonio))


# Subclasses possíveis: AgenciaVirtual; AgenciaComum; AgenciaPremium

# CRIANDO AS SUBCLASSES - NECESSÁRIO PASSAR A CLASSE MÃE COMO PARÂMETRO AO CRIAR.
# PARA INSTANCIAR: passar os parâmetros da classe mãe
# AO CRIAR UMA SUBCLASSE SEM O MÉTODO __init__, a subclasse importa o método herdado da classe pai
# Ao criar o __init__, dentro da subclasse, substitui o __init__ da classe pai - desconsiderando o __init__ da herança
# Para atribuir o __init__ da classe pai, necessário utilizar o super() e definir quais métodos devem ser executados na inicialização

# Cada classe também pode possuir seus métodos próprios
class AgenciaVirtual(Agencia):
  
  def __init__(self, site, telefone, cpnj):
    self.site = site
    super().__init__(telefone, cpnj, 1000)
    self.caixa = 1000000
    self.caixa_paypal = 0

  def depositar_paypal(self, valor):
    self.caixa -= valor
    self.caixa_paypal += valor

  def sacar_paypal(self, valor):
    self.caixa_paypal -= valor
    self.caixa += valor

# A classe AgenciaComumm irá utilizar automaticamente o mesmo __init__ da classe pai
class AgenciaComumm(Agencia):
  pass


# A classe AgenciaPremium irá atribuir automáticamente o nr da agência
# O método adicionar_cliente foi sobrescrito dentro da classe, mas aprovitou o método da classe pai
class AgenciaPremium(Agencia):

  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj, numero=randint(1001, 9999))
    self.caixa = 10000000

  def adicionar_cliente(self, nome, cpf, patrimonio):
    if patrimonio > 350000:
      super().adicionar_cliente(nome, cpf, patrimonio)
    else:
      print('Este cliente não possui patrimônio suficiente')


# OBSERVAÇÕES IMPORTANTES:
# SEMPRE REMOVER QUALQUER EXECUÇÃO DE CÓDIGO APÓS AS CLASSES, AFIM DE NÃO EXECUTAR AÇÕES INDESEJADAS
# OUTRA SOLUÇÃO É:

# Colocar if __name__ == '__main__' : e então colocar os testes dentro do main.

# Desta forma, o código somente será executado se eu executar a classe.
# Caso seja um import, não irá executar nos imports