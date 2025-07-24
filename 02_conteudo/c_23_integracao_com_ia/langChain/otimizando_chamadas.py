# https://www.mercadolivre.com.br/canon-eos-kit-t7-lente-18-55mm-is-ii-dslr-cor-preto/p/MLB18592482

reviews = ["Eu gostei bastante da câmera é a primeira vez que eu tiro foto com câmeras tirei algumas fotos não de pessoas no momento mas de algum objeto vou postar pra vocês verem",
           "Perfect!!! top de linha, vem com tudo que é descrito e ganhei um brinde maravilhoso. Verifiquei tudo, procedência etc etc. Tudo ok, não vão se arrepender!.",
           "Uma das melhores câmeras custo benefício para iniciantes da canon. Boa conectividade. Facilidade de aprender a mexer. Vale a pena pra quem não quer gastar muito mas quer ter câmera semi profissional.",
           "A apresentação da câmera é muito boa, mas preciso de uma câmera menor e mais compacta."]

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

class Avaliacao(BaseModel):
    "Review foi enviado por um cliente que comprou um produto, preciso avaliar esse produto para saber se ele é bom e se vale a pena"
    review_positiva: bool = Field(description="essa avaliação foi positiva ou negativa?")
    vale_pena: bool = Field(description="Essa avaliação no geral diz que vale a pena ou não vale a pena comprar esse produto?")
    pontos_positivos: list[str] = Field(description="quais os principais pontos positivos dessa avaliação? (cada ponto em no máximo 3 palavras, se houver)")
    pontos_negativos: list[str] = Field(description="quais os principais pontos negativos dessa avaliação? (cada ponto em no máximo 3 palavras, se houver)")

class ListaAvaliacoes(BaseModel):
    avaliacoes: list[Avaliacao] = Field(description="Lista com as avaliações de cada review")

parser = JsonOutputParser(name="avaliacao_usuario", pydantic_object=ListaAvaliacoes)
instrucoes = parser.get_format_instructions()
# print(instrucoes)

template_contexto = PromptTemplate.from_template("Você está avaliando reviews de vários usuários sobre um produto, preciso de algumas informações extraídas de cada review dessa lista de reviews: {reviews}")
template_idioma = PromptTemplate.from_template("Responda sempre em {idioma}", partial_variables={"idioma": "português"})
template_formato = PromptTemplate.from_template("Formato da resposta: {formato}", partial_variables={"formato": instrucoes})
template_final = (template_contexto + template_idioma + template_formato)

modelo = ChatOpenAI()

prompt = template_final.invoke({"reviews": reviews})
resposta = modelo.invoke(prompt)
resposta = parser.invoke(resposta)
print(resposta)

