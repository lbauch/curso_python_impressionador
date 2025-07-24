from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


modelo = ChatOpenAI()

template_chat = ChatPromptTemplate([
    SystemMessage("Responda o usuário sempre em {idioma} independente da língua que ele usar na pergunta")
], partial_variables={"idioma": "espanhol"})

texto_usuario = input("Digite a sua mensagem: ")

mensagem_usuario = HumanMessage(texto_usuario)
template_chat.append(mensagem_usuario)

prompt = template_chat.invoke({})
resposta = modelo.invoke(prompt)
parser = StrOutputParser()
resposta = parser.invoke(resposta)

print(resposta)
