# Importações de outros arquivos python.
from src.settings import *

# Importa a biblioteca de UI do discord.
from discord.ui import View, Select

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ABOUT
    @commands.hybrid_command(name = "about")
    async def about(self, ctx):
        embed = discord.Embed(
            title = "📑「 Informações do Bot 」📑",
            description = "",
            color = 0x5900FF
        )
        embed.add_field(
            name = "Nome:",
            value = "BlackHorizon™",
            inline = True
        )
        embed.add_field(
            name = "Versão:",
            value = "1.3.11",
            inline = True
        )
        embed.add_field(
            name = "Desenvolvedor:",
            value = "27prxblms (Xzhyan)",
            inline = True
        )
        embed.set_image(url = self.bot.user.avatar.url)
        await ctx.send(ctx.author.mention, embed = embed, delete_after = 30)
        await ctx.message.delete() # apaga a mensagem do autor do comando.

    # USER INFO
    @commands.hybrid_command(name = 'userinfo')
    @commands.check(AllowedChannels)
    async def userinfo(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title = "📑「 Informações do Usuário 」📑",
            description = "",
            color = 0x5900FF
        )
        embed.add_field(
            name = "Nome:",
            value = member.name,
            inline = True
        )
        embed.add_field(
            name = "ID:",
            value = member.id,
            inline = True
        )
        embed.add_field(
            name = "Criado em:",
            value = member.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            inline = True
        )
        embed.add_field(
            name = "Entrou em:",
            value = member.joined_at.strftime("%d/%m/%Y %H:%M:%S"),
            inline = True
        )
        embed.add_field(
            name = "Cargo dominante:",
            value = member.top_role,
            inline = True
        )
        embed.set_image(url = member.avatar.url)
        await ctx.send(ctx.author.mention, embed = embed, delete_after = 30)
        await ctx.message.delete() # apaga a mensagem do autor do comando.

    # CLEAR
    @commands.hybrid_command(name = 'clear')
    @commands.check(AllowedChannels)
    async def clear(self, ctx, clear_limit):

        # Verifica se o usuário digitou um número inteiro.
        if clear_limit.isdigit():
            clear_limit = int(clear_limit)

            if clear_limit <= 0:
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"Você não pode apagar `「 {clear_limit} 」` mensagens).",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

            elif clear_limit >= 101:
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"Desculpe o número máximo de mensagens que posso apagar por vez é `「 100 」`",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

            else:
                embed = discord.Embed(
                    title = "`🔄「 comando em execução! 🔄」`",
                    description = f"Preparando para apagar `「 {clear_limit} 」` mensagens.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
                await asyncio.sleep(5)
                await ctx.channel.purge(limit = clear_limit + 2)
                embed = discord.Embed(
                    title = "`✅「 comando finalizado! 」✅`",
                    description = f"Foi deletado `「 {clear_limit} 」` mensagens do chat.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

        # Se caso o usuário informe um text no lugar de um número inteiro.
        else:
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Você precisa informar um número inteiro junto ao comando.",
                color = 0x5900FF
            )
            await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

    # MENU / HELP
    @commands.hybrid_command(name = 'menu')
    @commands.check(AllowedChannels)
    async def menu(self, ctx):
        select = Select(
            min_values = 1, max_values = 1,
            placeholder = "🖥️   「 MENU 」   🖥️",
            options = [
                discord.SelectOption(
                    label = "Comandos Gerais",
                    value = "1",
                    emoji = "⚙️",
                    description = "ex: about, serverinfo, userinfo"
                ),
                discord.SelectOption(
                    label = "Comandos Administrativos",
                    value = "2",
                    emoji = "👨‍🔧",
                    description = "ex: kick, ban, roles"
                ),
                discord.SelectOption(
                    label = "Comandos Diversos",
                    value = "3",
                    emoji = "👽",
                    description = "ex: shoot, ping"
                ),
                discord.SelectOption(
                    label = "Comandos Ilegais",
                    value = "4",
                    emoji = "💉",
                    description = "ex: ipinfo, ddos"
                )
            ]
        )

        async def my_callback(interaction: discord.Interaction):
            # Menu de comandos - Gerais
            if select.values[0] == '1':
                embed = discord.Embed(
                    title = "🌌「 BlackHorizon™ Bot 」🌌",
                    description = f"Para usar os comandos do bot use `{prefix}` ou `/`.",
                    color = 0x5900FF
                )
                embed.add_field(
                    name = "• Lista de comandos:",
                    value = f"`{prefix}menu` Menu de comandos do bot.\n`{prefix}clear` Limpar/apagar mensagens.\n`{prefix}userinfo` Lista as informações do membro selecionado.\n`{prefix}about` Lista as informações do bot.",
                    inline = True
                )
                embed.set_thumbnail(url = imgbot)
                await interaction.response.edit_message(embed = embed)
                    
            # Menu de comandos - Admins
            if select.values[0] == '2':
                embed = discord.Embed(
                    title = "🌌「 BlackHorizon™ Bot 」🌌",
                    description = f"Para usar os comandos do bot use `{prefix}` ou `/`.",
                    color = 0x5900FF
                )
                embed.add_field(
                    name = "• Lista de comandos:",
                    value = f"`{prefix}kick` Expulsar membro do servidor.\n`{prefix}addrole` Adicionar cargos em um membro.\n`{prefix}removerole` Remover cargos de um membro.",
                    inline = True
                )
                embed.set_thumbnail(url = imgbot)
                await interaction.response.edit_message(embed = embed)

            # Menu de comandos - Diversos
            if select.values[0] == '3':
                embed = discord.Embed(
                    title = "🌌「 BlackHorizon™ Bot 」🌌",
                    description = f"Para usar os comandos do bot use `{prefix}` ou `/`.",
                    color = 0x5900FF
                )
                embed.add_field(
                    name = "• Lista de comandos:",
                    value = f"`{prefix}shoot` Atirar em um membro.",
                    inline = True
                )
                embed.set_thumbnail(url = imgbot)
                await interaction.response.edit_message(embed = embed)

            # Menu de comandos - Ilegais
            if select.values[0] == '4':
                embed = discord.Embed(
                    title = "🌌「 BlackHorizon™ Bot 」🌌",
                    description = f"Para usar os comandos do bot use `{prefix}` ou `/`.",
                    color = 0x5900FF
                )
                embed.add_field(
                    name = "• Lista de comandos:",
                    value = f"`{prefix}ipinfo` Mostra informações de um IP/Host.\n`{prefix}ddos` Mostra um site aleatório de Stresser/DDoS.",
                    inline = True
                )
                embed.set_thumbnail(url = imgbot)
                await interaction.response.edit_message(embed = embed)

        select.callback = my_callback
        view = View()
        view.add_item(select)

        # Embed do Menu Principal.
        embed = discord.Embed(
            title = "🌌「 BlackHorizon™ Bot 」🌌",
            description = "Selecione no menu a categoria de comandos que deseja ver.",
            color = 0x5900FF
        )
        embed.set_thumbnail(url = imgbot)
        await ctx.send(ctx.author.mention, embed = embed, view = view, delete_after = 30)
        await ctx.message.delete() # apaga a mensagem do autor do comando.

async def setup(bot):
    await bot.add_cog(General(bot))