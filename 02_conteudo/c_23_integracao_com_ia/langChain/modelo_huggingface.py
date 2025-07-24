from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import torch

torch.classes.__path__ = []


load_dotenv()

mensagens = [
    SystemMessage("Responda as perguntas de forma curta, mas não precisa ser tão curto. No máximo 140 caracteres")
]

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B")
modelo = ChatHuggingFace(llm=llm)

if __name__ == "__main__":
    mensagem_humano = input("Digite sua mensagem: ")

    mensagens.append(HumanMessage(mensagem_humano))

    resposta = modelo.invoke(mensagens)
    print(resposta)
    print(type(resposta))
    print(resposta.content)
    print(resposta.type)