from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

cliente = OpenAI()

# criar um audio para mim de acordo com um pedido/prompt
# resposta = cliente.chat.completions.create(
#     model="gpt-4o-audio-preview",
#     modalities=["text", "audio"],
#     audio={"format": "wav", "voice": "alloy"},
#     messages=[
#         {"role": "user", "content": "Crie um áudio convidando as pessoas para participarem da Jornada Python, uma jornada de aulas gratuitas onde elas aprendem a construir 4 projetos completos em Python partindo do zero"}
#     ]
# )

# gerar um áudio a partir de um texto
resposta = cliente.audio.speech.create(
    model="tts-1",
    voice="alloy",
    response_format="wav",
    input="Se você quer aprender Python e não sabe por onde começar, inscreva-se na Jornada Python da Hashtag"
)

print(resposta)

resposta.write_to_file("audio2.wav")

# faixa_audio = resposta.choices[0].message.audio.data
# faixa_audio_bytes = base64.b64decode(faixa_audio)

with open("audio.wav", "wb") as arquivo_audio:
    arquivo_audio.write(resposta.content)
