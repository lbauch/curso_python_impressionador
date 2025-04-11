from ContaCorrenteECartao import ContaCorrente, CartaoCredito
from Agencia import Agencia

conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)
cartao_lira = CartaoCredito('Lira', conta_Lira)
print(cartao_lira.conta_corrente.num_conta)
print(cartao_lira.conta_corrente._cartoes[0].numero)

print(cartao_lira.validade)

agencia1 = Agencia(111222333, 444555666, 4658)

agencia1.caixa = 1000000
agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 12345678910, 0.02)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Lucas', 123456789, 10000)
print(agencia1.clientes)