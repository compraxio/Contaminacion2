import discord
from discord.ext import commands
from Module import Clasificacion_tiempo_y_peligros, Datos_cientificos_y_consejos, Datos_de_contamincacion, recursos_para_manualidades
description = 'Una tarea😁'
intenciones = discord.Intents.default()
intenciones.message_content = True
bot = commands.Bot(command_prefix='/', description=description, intents=intenciones)
@bot.event
async def on_ready():
    print(f'Bot listo Hemos iniciado como {bot.user}\n------')
bot.run("Token")
