import streamlit as st
from modelo_huggingface import modelo, mensagens
from langchain_core.messages import HumanMessage, AIMessage

def abrir_chat(prompt, modelo, mensagens):
    if "mensagens" in st.session_state:
        mensagens = st.session_state["mensagens"]
    else:
        st.session_state["mensagens"] = mensagens
    if prompt:
        mensagens.append(HumanMessage(prompt))
        resposta = modelo.invoke(mensagens)
        conteudo_resposta = resposta.content
        if "</think>" in conteudo_resposta:
            mensagens.append(AIMessage(conteudo_resposta.split("</think>")[1]))
        else:
            mensagem.append(resposta)
    for mensagem in mensagens:
        if mensagem.type != "system":
            with st.chat_message(mensagem.type):
                st.write(mensagem.content)


def meu_app():
    st.header("HashGPT", divider=True)
    st.markdown("#### Converse com o ChatGPT integrado no Streamlit")
    prompt = st.chat_input("Digite a sua mensagem")
    abrir_chat(prompt, modelo, mensagens)


meu_app()