# PARA MAIS DETALHES, OLHAR A DOCUMENTAÇÃO DO IMAP TOOLS PYTHON

#!pip install imap-tools
from imap_tools import MailBox, AND

usuario = "seuemail@gmail.com"
# Senha para apps
senha = "sua_senha_app_aqui"

# Configurar o servidor e email - para encontrar o servidor, procurar servidor imap no google
meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# ver as pastas do meu email disponíveis
# for pasta in meu_email.folder.list():
#     print(pasta)

# meu_email.folder.set('[Gmail]/E-mails enviados')

# Ao pegar os emails desta forma, traz os dados como um generator:
# Generator é similar a uma lista que armazena os emails como objetos
# Para utilizá-los, é necessário pegar cada email individualmente
lista_emails = meu_email.fetch(AND(from_="emailremetente@gmail.com", to="emaildestinatario@hotmail.com"))
# print(list(lista_emails))

# Pode ser utilizado como um iterable e ser percorrido
for email in lista_emails:
    if len(email.attachments) > 0:
        # Lê o título do email
        print(email.subject)
        # Lê o texto do email que não está em html
        print(email.text)
        # Lê o html
        print(email.html)
        # Anexos do email
        for anexo in email.attachments:
            print("Anexo:", anexo.filename)
