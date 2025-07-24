import streamlit as st
import random

lista_resposta = ["OK", "Legal", "Tudo bem", "Tem certeza?"]

def app():
    st.header("Hash Chat", divider=True)
    st.write("### Escreva e interaja com o nosso chat ao vivo")

    mensagem_usuario = st.chat_input("Digite aqui sua mensagem")
    if mensagem_usuario:
        if "mensagens" in st.session_state:
            mensagens = st.session_state["mensagens"]
        else:
            mensagens = []
            st.session_state["mensagens"] = mensagens

        # adicionar no mensagens a mensagem que o usuário enviou
        mensagens.append({"usuario": "user", "texto": mensagem_usuario})

        # mensagem de resposta do assistant
        resposta = random.choice(lista_resposta)
        mensagens.append({"usuario": "assistant", "texto": resposta})

        for mensagem in mensagens:
            # colocar a mensagem do usuário na tela
            with st.chat_message(mensagem["usuario"]):
                st.write(mensagem["texto"])

app()