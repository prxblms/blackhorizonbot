#from discord.ext.commands.errors import CommandNotFound
#from discord.ext.commands.errors import MissingRequiredArgument
#from discord.ext.commands.errors import MissingAnyRole
#from discord.ext.commands.errors import CheckFailure

# Importações de outros arquivos python.
from src.settings import *

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Interações de erro no bot.
    @commands.Cog.listener()
    async def on_command_error(self, message, error):

        # Não permite o uso de comandos nesse chat.
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Não é permitido o uso de comandos nesse chat.",
                color = 0x5900FF
            )
            await message.send(message.author.mention, embed = embed, delete_after = 10)
            await message.message.delete()

        # Comando não existe.
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"O comando que você esta tentando usar não existe.",
                color = 0x5900FF
            )
            await message.send(message.author.mention, embed = embed, delete_after = 10)

        # Erro de interação.
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError) and isinstance(error.original, asyncio.TimeoutError):
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Desculpe, a interação demorou para ser concluída. Por favor, tente novamente..",
                color = 0x5900FF
            )
            await message.send(message.author.mention, embed = embed, delete_after = 10)

        # Usuário não tem permissão.
        if isinstance(error, commands.MissingAnyRole):
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Você não tem permissão para usar esse comando.",
                color = 0x5900FF
            )
            await message.send(message.author.mention, embed = embed, delete_after = 10)

        # Argumento faltando.
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = f'{error}'[:-40]

            # CLEAR LIMIT
            if arg_error == 'clear_limit':
                embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = "Você precisa informar o número de mensagens que deseja apagar.",
                color = 0x5900FF
                )
                embed.add_field(
                    name = f"Exemplo:",
                    value = f"`{prefix}clear 10`\n`{prefix}clear 100`",
                    inline = True
                )
                await message.send(message.author.mention, embed = embed, delete_after = 10)

            # MEMBRO
            if arg_error == 'member':
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = "Você precisa informar um membro para completar esse comando.",
                    color = 0x5900FF
                )
                await message.send(message.author.mention, embed = embed, delete_after = 10)

            # MOTIVO
            if arg_error == 'motivo':
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = "Você precisa informar o motivo da expulsão.",
                    color = 0x5900FF
                )
                await message.send(message.author.mention, embed = embed, delete_after = 10)

            # IP INFO
            if arg_error == 'ip':
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"Você precisa informar um IP ou Host junto ao comando.\nExemplos:\n`{prefix}ipinfo` 1.1.1.1 | `{prefix}ipinfo` google.com\n`/ipinfo` 1.1.1.1 | `/ipinfo` google.com",
                    color = 0x5900FF
                )
                await message.send(message.author.mention, embed = embed, delete_after = 10)

        else:
            raise error

async def setup(bot):
    await bot.add_cog(Errors(bot))