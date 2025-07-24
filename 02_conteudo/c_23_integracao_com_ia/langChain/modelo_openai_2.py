from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts.chat import MessagesPlaceholder

template_chat = ChatPromptTemplate(
    [
        SystemMessage("Responda o usuário com respostas diretas e o mais curtas possíveis, mas sempre respondendo a dúvida dele. As dúvidas são referentes a programação em {tema}. Qualquer outra dúvida que não seja desse tema apenas responda: não sou especialista no tema"),
        MessagesPlaceholder("history")
    ], partial_variables={"tema": "Python"}
)

modelo = ChatOpenAI()

chain = template_chat | modelo
