# Importações de outros arquivos python.
from src.settings import discord, random, music_list

# Função para mudar as musicas que o bot esta ouvindo.
async def MusicActivity(bot):
    #activity = discord.Game(random.choice(BotAtividades))
    activity = discord.Activity(type = discord.ActivityType.listening, name = random.choice(music_list))
    await bot.change_presence(activity = activity)

# New Activity
# @tasks.loop(hours = 6)
# async def AutoSendMessage():
#     channel = bot.get_channel(1098993587699585257)
#     await channel.send("@everyone https://youtu.be/9Kz9cUGWlIw")