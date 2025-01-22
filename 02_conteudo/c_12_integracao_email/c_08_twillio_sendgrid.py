# API
# Envio de emails em massa
# Necessário este serviço para não ser bloqueado e não cair em span.
# Forma autenticada e segura

# Criar conta no Twillio
# Configurar sender - single sender verification
# Recomendado não utilizar email próprio, mas email de empresa
# No sendgrid, configurar web api - selecionar linguagem de prog uilizada criar chave de api
# Isso gera uma chave de api

# - Requisições (requests, get, post, patch, delete)

# - Biblioteca (sendgrid)

#!pip install sendgrid
chave_api_sendgrid = "sua_chave_api"

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

# email passado deve estar em algum dos emails criados no Twillio
# to_emails - caso seja email único, pode ser string. Para mais, fazer lista
# Evitar anexos em emails em massa - enviar link ao invés.
email = Mail(from_email="seuremetente@gmail.com", to_emails=['seu_destinatario@hotmail.com','seu_destinatario2@hotmail.com'], 
             subject="Email enviado pelo Sendgrid no Python", 
             html_content="<p>Email enviado com sucesso, seja bem vindo</p><p>Abraços e até o próximo e-mail.</p>")

# Para mais funcionalidades, acessar a documentação
resposta = conta_sendgrid.send(email)
print(resposta.status_code)


