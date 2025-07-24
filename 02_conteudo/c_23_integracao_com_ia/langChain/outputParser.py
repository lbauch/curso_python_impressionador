# gerador de base de dados
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser


modelo = OpenAI()
parser = CommaSeparatedListOutputParser()

template_forma = PromptTemplate.from_template("Formato da resposta: {formato}", partial_variables={"formato": parser.get_format_instructions()})
template_idioma = PromptTemplate.from_template("Os textos da sua resposta devem estar em {idioma}", partial_variables={"idioma": "espanhol"})
template_mensagem = PromptTemplate.from_template("Mensagem do usuário: {mensagem}")
template_final = (template_forma + template_idioma + template_mensagem)

prompt = template_final.invoke({"mensagem": "Gere uma lista com o nome de 10 clientes"})

resposta = modelo.invoke(prompt)


resposta = parser.invoke(resposta)
print(resposta)