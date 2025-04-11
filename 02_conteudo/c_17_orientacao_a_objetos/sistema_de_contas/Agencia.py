from random import randint

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

# Deve chamar o __init__ da classe pai, usando super() e passar os atributos no método
class AgenciaVirtual(Agencia):
  
  def __init__(self, site, telefone, cpnj):
    self.site = site
    super().__init__(telefone, cpnj, 1000)
    self.caixa = 5500000
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
class AgenciaPremium(Agencia):

  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj, numero=randint(1001, 9999))
    self.caixa = 10000000
