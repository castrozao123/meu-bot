import discord
from discord.ext import commands
import asyncio
import os
TOKEN = os.getenv("TOKEN")

# Adiciona aqui o ID de cada canal de anúncios de cada servidor
CANAIS_ANUNCIO = [
    1495448198771118130,   # Tequilas
    1495458532412100648,   # Redline
    1495469248825262090,   # Layboy
    1445179554019803321,   # Testes
]
# --------------------

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot ligado como {bot.user}")
    print(f"📡 A monitorizar {len(CANAIS_ANUNCIO)} canais de anúncios")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in CANAIS_ANUNCIO:
        guild = message.guild
        enviados = 0
        falhados = 0

        print(f"📢 Anúncio em '{guild.name}'! A enviar PV a todos os membros...")

        for member in guild.members:
            if member.bot:
                continue
            if member.id == message.author.id:
                continue

            try:
                await member.send(
                    f"📢 **Novo anúncio em {guild.name}:**\n\n"
                    f"{message.content}\n\n"
                    f"— {message.author.display_name}"
                )
                enviados += 1
                await asyncio.sleep(1)

            except discord.Forbidden:
                falhados += 1
            except discord.HTTPException as e:
                print(f"Erro ao enviar para {member}: {e}")
                falhados += 1

        print(f"✅ [{guild.name}] Enviados: {enviados} | ❌ Falhados: {falhados}")

    await bot.process_commands(message)


bot.run("MTQ5NTQ0MjU1ODIwODQ0MjU4MA.GfWbGV.NuLvE3VrI6RE06W0lYf3HJ48NxJ_3SH7lpnZvM")
