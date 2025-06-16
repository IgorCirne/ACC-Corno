import discord
import asyncio
import os
import random
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# Carregar variáveis do .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
USER_ID = int(os.getenv("USER_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Lista de mensagens possíveis
mensagens = [
    "{user.mention} o cleave te espera",
    "Se ligue não viu {user.mention}, Wow vai fazer seu pinto ficar pequeno ",
    "{user.mention}",
    "{user.mention} You should Kill YOURSELF NOW",
    "{user.mention} A cada segundo que você não está correndo, eu estou chegando mais perto, o fim do mundo se aproxima e você não cleava mais com os brother, um dia você estará sozinho, implorando pela presençados outros, e só então eu irei olhar diretamente nos seus olhos e dizer: SE FODEU OTARIO",
    "{user.mention} Um dia você irá sucumbir ao peso de seus pecados, e não vai ter ninguém para te ajudar"
]

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')
    await start_mention_loop()


async def start_mention_loop():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)
    user = guild.get_member(USER_ID)

    if channel is None or user is None:
        print("Canal ou usuário não encontrado!")
        return

    while not client.is_closed():
        try:
            # Escolhe uma mensagem aleatória
            mensagem = random.choice(mensagens).format(user=user)
            await channel.send(mensagem)

            # Espera 1 hora (3600 segundos)
            await asyncio.sleep(3600)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            await asyncio.sleep(60)  # Espera 1 min antes de tentar de novo


client.run(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Estou vivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()