# Importações de outros arquivos python.
from src.settings import *

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # Caso a mensgem seja envida pelo bot, ele ignora ela.
        if message.author == self.bot.user:
            return
        
        # Resposta de quando o bot é mencionado por alguém.
        if f'{self.bot.user.id}' in message.content:
            embed = discord.Embed(
                title = "`「 Olá amigo! 」`",
                description = f"Caso você tenha dúvidas sobre os comandos do bot use:\n`「 {prefix}menu 」` ou `「 /menu 」`.",
                color = 0x5900FF
            )
            await message.channel.send(message.author.mention, embed = embed, delete_after = 10)

        else:
            return

async def setup(bot):
    await bot.add_cog(Messages(bot))