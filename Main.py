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
    "{user.mention} Tell me. For whom do you fight? Hmph! How very glib. And do you believe in Eorzea? Eorzea's unity is forged of falsehoods. Its city-states are built on deceit. And its faith is an instrument of deception. Are the Twelve otherwise engaged? I was given to understand they were your protectors. If you truly believe them your guardians, why do you not repeat the trick that served you so well at Carteneau, and call them down? They will answer--so long as you lavish them with crystals and gorge them on aether. Your gods are no different than those of the beasts--eikons every one. Accept but this, and you will see how Eorzea's faith is bleeding the land dry. Nor is this unknown to your masters. Which prompts the question: Why do they cling to these false deities? What drives even men of learning--even the great Louisoix--to grovel at their feet? The answer? Your masters lack the strength to do otherwise! For the world of man to mean anything, man must own the world. To this end, he hath fought ever to raise himself through conflict--to grow rich through conquest. And when the dust of battle settles, is it ever the strong who dictate the fate of the weak.Knowing this, but a single path is open to the impotent ruler--that of false worship. A path which leads to enervation and death. Only a man of power can rightly steer the course of civilization. And in this land of creeping mendacity, that one truth will prove its salvation.Come, champion of Eorzea, face me! Your defeat shall serve as proof of my readiness to rule! It is only right that I should take your realm. For none among you has the power to stop me!"
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