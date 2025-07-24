import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from modelo_openai import chain

    
def abrir_chat(prompt):
    if prompt:
        mensagens = [HumanMessage(prompt)]
        
        for mensagem in mensagens:
            if mensagem.type != "system":
                with st.chat_message(mensagem.type):
                    st.write(mensagem.content)

            
def meu_app():
    st.header("Hash Rei do Python", divider=True)
    st.markdown("#### Tire suas dúvidas sobre Python")
    prompt = st.chat_input("Digite aqui seu prompt")
    abrir_chat(prompt)
    

        

if __name__ == "__main__":
    meu_app()


