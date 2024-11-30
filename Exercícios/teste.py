precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    precos[produto] = novo_preco
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")