from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

cliente = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct")

prompt = "What is Python programming language?"

resposta = cliente.text_generation(prompt)

print(resposta)

