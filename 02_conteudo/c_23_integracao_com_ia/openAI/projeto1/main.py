from legendador import legendar
import streamlit as st

# legenda = legendar("ja começou a jornada full stack.mp4", contexto="Esse áudio é de um anúncio da Jornada Full Stack da Hashtag, um conteúdo completaço sobre desenvolvimento")

def meu_app():
    st.header("Hash Legendador", divider=True)
    st.markdown("#### Gere a legenda de qualquer vídeo ou áudio automaticamente")

    contexto = st.text_input("Dê algum contexto do que o vídeo se trata para ajudar na legenda")
    arquivo = st.file_uploader("Selecione o vídeo (.mp4) ou o áudio (.mp3) para legendar", type=["mp4", "mp3"])
    if arquivo:
        legenda = legendar(arquivo, contexto)
        st.write(f"Arquivo {arquivo.name} legendado com sucesso")
        st.write(legenda)

if __name__ == "__main__":
    meu_app()