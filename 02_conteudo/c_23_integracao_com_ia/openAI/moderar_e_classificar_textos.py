from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()

resposta = cliente.moderations.create(
    model="omni-moderation-latest",
    input="O Lira é muito burro, não sabe nada de Python"
)

moderacao = resposta.results[0]

print(moderacao.flagged)
print(moderacao.categories.to_dict())

