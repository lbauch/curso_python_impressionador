from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

cliente = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct")

mensagens = [
    {"role": "system", "content": "Responda as perguntas de forma correta e precisa"},
]

while True:
    prompt = input("Digite a sua mensagem: ")
    mensagem_usuario = {"role": "user", "content": prompt}
    mensagens.append(mensagem_usuario)

    resposta = cliente.chat_completion(mensagens)

    resposta_ia = resposta.choices[0]
    role_resposta = resposta_ia.message.role
    content_resposta = resposta_ia.message.content

    dicionario_resposta_ia = {"role": role_resposta, "content": content_resposta}
    mensagens.append(dicionario_resposta_ia)

    print("IA:", content_resposta)


