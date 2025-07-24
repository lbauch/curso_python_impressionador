from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

conversas = {}
def pegar_sessao(session_id):
    if session_id not in conversas:
        conversas[session_id] = InMemoryChatMessageHistory()
    return conversas[session_id]


template_chat = ChatPromptTemplate(
    [
        ("system", "Responda o usuário com respostas diretas e o mais curtas possíveis, mas sempre respondendo a dúvida dele. As dúvidas são referentes a programação em {tema}. Qualquer outra dúvida que não seja desse tema apenas responda: não sou especialista no tema"),
        ("placeholder", "{history}"),
        ("user", "{mensagem}")
    ], partial_variables={"tema": "Python"}
)

modelo = ChatOpenAI()

chain = template_chat | modelo
chain_memoria = RunnableWithMessageHistory(chain, 
                                           get_session_history=pegar_sessao,
                                           input_messages_key="mensagem",
                                           history_messages_key="history")
