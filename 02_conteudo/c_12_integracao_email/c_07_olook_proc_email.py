import win32com.client as win32
import os

# Utiliza o Outlook Desktop
outlook = win32.Dispatch("outlook.application")

# MAPI é referente ao IMAP
# Mostra todas as contas conectadas
caixas_email = outlook.GetNamespace("MAPI")

# ver todas as dontas do email conectadas
# for pasta in caixas_email.Folders:
#     print(pasta)

# O índice indica a conta que será uilizada - índice inicia em 1
pasta_python = caixas_email.Folders.Item(2)

# Verificar todas as subpastas (caixas) de uma conta específica
# for subpasta in pasta_python.Folders:
#     print(subpasta)

# Pega a caixa de entrada da conta selecionada
# Items(1) indica o nr da caixa de entrada
caixa_entrada = pasta_python.Folders.Item(1)

# Lista de todos os emais
lista_emails = caixa_entrada.Items

print(len(lista_emails))

for email in lista_emails:
    anexos = email.Attachments
    if email.To == "seuemaildestino@hotmail.com" and len(anexos) > 0:
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        for anexo in anexos:
            print(anexo.FileName)
            caminho_codigo = os.getcwd()
            caminho_anexo_salvar = os.path.join(caminho_codigo, f"Email {email.Subject} - {anexo.FileName}")
            anexo.SaveAsFile(caminho_anexo_salvar)

print("Fim do código")