
#pip install pywin32
import win32com.client as win32
import os

# Nome do apllicativo desktop do outlook é outlook.application, excel é excel.application
outlook = win32.Dispatch("outlook.application")

# O índice 0 dentro de CreateItem indica a criação de um email.
# É possível criar novas pastas e outras diversas funconalidades - olhar documentação
email = outlook.CreateItem(0)

# Para olhar todas as propriedades que se quer, pode-se utilizar o debugger (dentro  do VSCode)
# pausar o debugger após a criação do email e olhar special_variables
# Destinatário
email.To = "seuemaildestino@hotmail.com"
# Todos os com cópia
email.Cc = "seuemailcopia@gmail.com;outroemailcopia@hotmail.com"
# Cópia oculta
email.Bcc = "outroemailcopiaoculta@gmail.com"
email.Subject = "Email enviado pelo Outlook"
# email.Body = "raw text - Texto do email"
email.HTMLBody = """<p>Meu primeiro paragrafo</p>
<p>Outro paragrafo no email</p>
<img src='seu_link_imagem'
width=200>"""
# CASO QUEIRA INSERIR O ARQUIVO DO COMPUTADOR: deve ser utilizado o caminho completo do arquivo, SEMPRE
# Link de imagem da internet

# Pegar pasta na qual está sendo executado o arquivo em python:
caminho_codigo = os.getcwd()
arquivo_anexar = "anexos/kivy.png"

# Juntar caminhos
# os.path.join(caminho_codigo,arquivo_anexar)
lista_arquivos = os.listdir("anexos")

for nome_arquivo in lista_arquivos:
    caminho_anexo = os.path.join(caminho_codigo, "anexos", nome_arquivo)
    # Inserir no email o arquivo
    email.Attachments.Add(caminho_anexo)

# Envia o email
email.Send()