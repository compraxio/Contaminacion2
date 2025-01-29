import discord
from discord.ext import commands
description = 'Una tarea😁'
intenciones = discord.Intents.default()
intenciones.message_content = True
bot = commands.Bot(command_prefix='#', description=description, intents=intenciones)
@bot.event
async def on_ready():
    print(f'Bot listo Hemos iniciado como {bot.user}\n------')
bot.run("Token")
