# SMTP

# Integração feita com gmail, por ser mais fácil. Outros emails demandam mais configurações
# Para replicar, é possível só copiar o arquivo e fazer as alterações
import smtplib
import email.message

def enviar_email():
    
    msg = email.message.Message()
    # Título
    msg["Subject"] = "Email enviado com Python"
    # Remetente
    msg["From"] = "seuemail@gmail.com"
    # Destinatário
    msg["To"] = "seuemaildestino@gmail.com"
    # Com cópia - separa os emails com ;
    msg["Cc"] = "seuemailcopia@gmail.com;outroemailcopia@hotmail.com"
    # Cópia oculta
    msg["Bcc"] = "seuemailcopiaoculta@gmail.com"
    
    link_imagem = "coloque_aqui_o_link_da_sua_imagem"

    # Necessário fazer em html
    corpo_email = f"""<p>Boa tarde,</p>
    <p>Esse é meu primeiro email com Python usando smtplib</p>
    <p>Att., Lira</p>
    <img src='{link_imagem}'>"""
    # Pode ser utilizado para inserir assinatura de email - links de internet

    # Necessário encode para utf-8 para garantir formatação
    corpo_email = corpo_email.encode("utf-8")

    # Adiciona o header e payload
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    # servidor = smtplib.SMTP(servidor, porta) - para dúvidas, consultar internet
    # Em alguns casos, pode ser necessário ter que liberar a conexão no próprio email
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    # starttls é o formato de criptografia utilizada entre emails
    servidor.starttls()
    # Configurar login e senha
    # Como o usuário que envia é o mesmo que o remetente do email, é possível utilizar a mesma variável.
    # Não passar a senha verdadeira, por ser menos seguro. Passar uma senha específica para apps.
    """
    Como fazer com gmail: Gerenciar conta Google - procurar por senha e ir na opção senha de apps 
    Digitar a senha desejada e copiar a senha criptografada
    Configurar email e senha em variáveis de ambiente
    """
    servidor.login(msg["From"], "sua_senha_app")
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado")


enviar_email()