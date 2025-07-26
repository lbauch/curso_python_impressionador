import tkinter as tk

janela = tk.Tk()

janela.title("Cota��o de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cota��o de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


dicionario_cotacoes = {
    'D�lar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="Cota��o n�o encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cota��o do {moeda_preenchida} � de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar Cota��o", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()


