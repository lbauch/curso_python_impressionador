from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

modelo = OpenAI()

template_prompt = PromptTemplate.from_template("""Responda ao usuário em no máximo {tamanho} caracteres, responda em {idioma}, independente da língua que o usuário fizer a pergunta.
Pergunta do usuário: {mensagem}
""")

prompt = template_prompt.invoke({"tamanho": 140, "idioma": "espanhol", "mensagem": "Python vale a pena aprender para quem não sabe nada?"})


resposta = modelo.invoke(prompt)
print(resposta)
