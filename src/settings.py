import json
import discord
import random
import asyncio
import os
import requests
from discord.ext import commands
from discord.ext import tasks

# Carregar as configurações do config.json.
with open('src/config.json') as config_file:
    bot_config = json.load(config_file)
# Seta os valores do config.json para as variaveis.
token = bot_config['token']
prefix = bot_config['prefix']
imgbot = bot_config['imgbot']

# API Keys:
tenor_api_key = 'AIzaSyAEfholSIYKsmwPrsuMIWP6iJilVKW10z0'

# Variaveis de atividades do Bot:
music_list = ['Xzhyan - Mente Ruim', 'Xzhyan - Nxsleep', 'Xzhyan - Mais uma Noite', 'Dr. Who! - Daleks Diss ft. Boe']

# Variaveis de IDs do discord:
guild_id = 1064984065335369810

# Canais onde é permitido o uso de comandos.
# After Dawn Community:
comandos = 1178822345452965949
general = 1178810701263949846
# Laboratorio de bots:
testes = 1195435406741733528
# Seta a ID dos canais para a lista 'allowed_channels'.
allowed_channels = [comandos, testes, general]

# Função para verificar os canais que permitem uso de comandos.
def AllowedChannels(ctx):
    if ctx.channel.id in allowed_channels:
        return ctx.channel.id in allowed_channels

# Lista de gifs do comando shoot.
shoot_gif_1 = 'https://media4.giphy.com/media/PnhOSPReBR4F5NT5so/giphy.gif?cid=6c09b9529y4jy1tbw1mgnhrw8xbeuvls7e7gjnf2vnb8x87z&ep=v1_gifs_search&rid=giphy.gif&ct=g'
shoot_gif_2 = 'https://j.gifs.com/E8pPnk.gif'
shoot_gif_3 = 'https://media1.tenor.com/m/K6aPMqQsGkUAAAAC/shoot-gift.gif'
shoot_gif_4 = 'https://media0.giphy.com/media/lrPDCZOAwf2S0k7B8R/giphy.gif'
shoot_gif_5 = 'https://i.pinimg.com/originals/fb/15/62/fb1562f66478f24a354ecc883318c7cb.gif'
shoot_gif_6 = 'https://j.gifs.com/vnORbe.gif'
shoot_gifs = [shoot_gif_1, shoot_gif_2, shoot_gif_3, shoot_gif_4, shoot_gif_5, shoot_gif_6]