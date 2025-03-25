
# Como a classe não possui parâmetros, não é necessário o parênteses na classe
# class ContaCorrente: também estaria correto
class ContaCorrente():

  def __init__(self, nome, cpf):
    self.nome = nome
    self.cpf = cpf
    self.saldo = 0
    # Definido após criação inicial
    self.limite = None

  def consultar_saldo(self):
    print('seu saldo atual é de R${:,.2f}'.format(self.saldo).replace(',','_').replace('.',',').replace('_','.'))

  def depositar(self, valor):
    self.saldo += valor
    self.consultar_saldo()

  # Inicialmente, este método estava sendo criado, mas o limite não era instanciado na criação da classe.
  # Fazer como o comentário acima não é recomendado
  # Métodos com underline no início são definidos como privados e não devem ser utilizados fora da classe
  def _limite_conta(self):
    self.limite = -1000
    return self.limite

  def sacar_dinheiro(self, valor):
    if self.saldo - valor < self._limite_conta():
      print('Você não tem saldo suficiente para sacar este valor')
      self.consultar_saldo()
    else:
      self.saldo -= valor
      self.consultar_saldo()

  def consultar_limite_chequeespecial(self):
    print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))
# Ao finalizar a construção de uma classe, deixa-se 2 "enter" após o fim.
# Entre os métodos, deixa-se 1 "enter".


# Programa
conta_Lira = ContaCorrente('Lira','111.222.333-44')

print(conta_Lira.cpf)
# print(conta_Lira.saldo)
conta_Lira.consultar_saldo()

conta_Lira.depositar(1000)

conta_Lira.sacar_dinheiro(1500)