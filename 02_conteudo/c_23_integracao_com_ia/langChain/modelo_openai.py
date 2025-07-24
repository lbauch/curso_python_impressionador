from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

mensagens = [
    SystemMessage("Responda as perguntas de forma curta, mas não precisa ser tão curto. No máximo 140 caracteres")
]

modelo = ChatOpenAI()

if __name__ == "__main__":
    mensagem_humano = input("Digite sua mensagem: ")

    mensagens.append(HumanMessage(mensagem_humano))

    resposta = modelo.invoke(mensagens)
    print(resposta)
    print(type(resposta))
    print(resposta.content)
    print(resposta.type)