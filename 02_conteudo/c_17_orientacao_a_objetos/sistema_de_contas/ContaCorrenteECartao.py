from datetime import datetime
import pytz
from random import randint


class ContaCorrente:

  @staticmethod
  def _data_hora():
    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

  def __init__(self, nome, cpf, agencia, num_conta):
    self.nome = nome
    self.cpf = cpf
    self.saldo = 0
    self.limite = None
    self.agencia = agencia
    self.num_conta = num_conta
    self._senha = '1234'
    self.transacoes = []
    self._cartoes = []

  def consultar_saldo(self):
    print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

  def depositar(self, valor):
    self.saldo += valor
    self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

  def _limite_conta(self):
    self.limite = -1000
    return self.limite

  def sacar_dinheiro(self, valor):
    if self.saldo - valor < self._limite_conta():
      print('Você não tem saldo suficiente para sacar esse valor')
      self.consultar_saldo()
    else:
      self.saldo -= valor
      self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

  def consultar_limite_chequeespecial(self):
    print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))

  def consultar_historico_transacoes(self):
    print('Histórico de Transações:')
    print('Valor, Saldo, Data e Hora')
    for transacao in self.transacoes:
      print(transacao)

  def transferir(self, valor, conta_destino):
    self.saldo -= valor
    self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
    conta_destino.saldo += valor
    conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

  # Atenção à forma de criação do getter e setter
  # Devem ter o mesmo nome de método, recebendo parâmetros diferentes e com decorators diferentes

  # GETTER - Criando o getter de senha (Esta linha de comentário de código não é necessária)
  # Necessário o decorator
  @property
  def senha(self):
    return self.senha
  
  # SETTER - Criando o setter de senha (Esta linha de comentário de código não é necessária)
  # Necessário o decorator
  @senha.setter
  def senha(self, senha):
    if len(senha) == 4 and senha.is_numeric():
      self._senha = senha
    else:
      print('Senha nova inválida, senha anterior mantida')

class CartaoCredito:

  @staticmethod
  def _data_hora():
    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR

  def __init__(self, titular, conta_corrente):
    self.numero = randint(100000000000000, 999999999999999)
    self.titular = titular
    self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 1)
    self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
    self.limite = 1000
    self.conta_corrente = conta_corrente
    conta_corrente._cartoes.append(self)
    # Outra opção seria utilizar:
    # conta_corrente._cartoes.append(self.numero)
