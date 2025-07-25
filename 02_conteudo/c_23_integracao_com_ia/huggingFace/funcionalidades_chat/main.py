import streamlit as st
from hfapi_summarization import resumir
from hfapi_textgeneration import gerar_texto
from hfapi_chatcompletion import completar_chat

def gerador_texto(prompt):
    st.markdown("##### Peça para o sistema gerar um texto para você")
    if prompt:
        texto_resposta = gerar_texto(prompt)
        st.write(texto_resposta)

def resumidor_texto(prompt):
    st.markdown("##### Cole na caixa de prompt o texto que deseja resumir")
    if prompt:
        texto_resposta = resumir(prompt)
        st.write(texto_resposta)

def abrir_chat(prompt):
    st.markdown("##### Converse com a IA da Hashtag")

    # armazenar a lista de mensagens -> session_state
    mensagens = [
        {"role": "system", "content": "Responda as perguntas de forma correta e precisa"},
    ]

    if prompt:
        mensagem_usuario = {"role": "user", "content": prompt}
        mensagens.append(mensagem_usuario)
        mensagens = completar_chat(mensagens)
        print(mensagens)
        # exibir as mensagens em formato de chat

def main_app():
    # titulo -> HashIAs
    st.header("HashIAs", divider=True)
    # subtitulo -> Selecione a IA que mais te ajuda, envie seu prompt e seja feliz
    st.markdown("#### Selecione a IA que mais te ajuda, envie seu prompt e seja feliz")
    # selectbox -> Gerar Texto, Resumir Texto, Abrir Chat
    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    ferramenta_selecionada = st.selectbox("Selecione a ferramenta de IA que você vai usar", options=opcoes)
    
    # Campo de prompt -> Digite aqui seu prompt
    prompt = st.chat_input("Digite aqui seu prompt")

    if ferramenta_selecionada:
        if ferramenta_selecionada == opcoes[0]:
            gerador_texto(prompt)
        elif ferramenta_selecionada == opcoes[1]:
            resumidor_texto(prompt)
        else:
            abrir_chat(prompt)


main_app()