import discord 
from discord.ext import commands
import urllib
from urllib import parse, request
import re

# comentario de prueba
cliente = commands.Bot (command_prefix = '!')

@cliente.event
async def on_ready():
    print ("El bot esta listo")

@cliente.command()
async def buscador(ctx, *, search):
    consulta = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + consulta)
    resultados_busqueda = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(resultados_busqueda)
    await ctx.send('https://www.youtube.com/watch?v=' + resultados_busqueda[0])

cliente.run('ODA1Mjc3NDk3OTg1MzM1MzE2.YBYjHA.EkT3eAnCGM9T3o1nMrbSuu0F5w4')