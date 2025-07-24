import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from modelo_openai import chain_memoria


def abrir_chat(prompt, chain):
    if "mensagens" in st.session_state:
        mensagens = st.session_state["mensagens"]
    else:
        mensagens = []
        st.session_state["mensagens"] = mensagens

    if prompt:
        mensagens.append(HumanMessage(prompt))
        resposta_ia = chain.invoke({"history": mensagens})
        mensagens.append(resposta_ia)

        for mensagem in mensagens:
            if mensagem.type != "system":
                with st.chat_message(mensagem.type):
                    st.write(mensagem.content)

            
def meu_app():
    st.header("Hash Rei do Python", divider=True)
    st.markdown("#### Tire suas dúvidas sobre Python")
    prompt = st.chat_input("Digite aqui seu prompt")
    abrir_chat(prompt, chain)
    

        

if __name__ == "__main__":
    meu_app()


