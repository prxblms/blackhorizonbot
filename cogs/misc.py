# Importações de outros arquivos python.
from src.settings import *

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # SHOOT
    @commands.hybrid_command(name = "shoot")
    @commands.check(AllowedChannels)
    async def shoot(self, ctx, member: discord.Member):
        random_gif = random.choice(shoot_gifs)
        embed = discord.Embed(
            title = "Pow pow !!!",
            description = f"**{ctx.author.mention} ACABOU DE ATIRAR EM VOCÊ!!!**",
            color = 0xF3FF00
        )
        embed.set_image(url = random_gif)
        await ctx.send(member, embed = embed)
        await ctx.message.delete() # apaga a mensagem do autor do comando.

async def setup(bot):
    await bot.add_cog(Misc(bot))