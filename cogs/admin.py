# Importações de outros arquivos python.
from src.settings import *

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # REMOVE ROLE
    @commands.hybrid_command(name = 'removerole')
    @commands.check(AllowedChannels)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):

        # Verifica se o usuário que usou o comando tem permissão.
        ctx_member = ctx.guild.get_member(ctx.author.id)
        if ctx_member.guild_permissions.administrator:
            
            member = ctx.guild.get_member(member.id)
            get_roles = member.roles
            role_names = [role.name for role in get_roles]
            role = ctx.guild.get_role(role.id)

            if role.name in role_names:
                await member.remove_roles(role)
                embed = discord.Embed(
                    title = "`✅「 comando finalizado! 」✅`",
                    description = f"O membro {member} teve o cargo de {role} removido.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

            else:
                await member.add_roles(role)
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"O membro {member} não possuí o cargo {role}.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

        # Usuário não tem permissão.
        else:
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Você não tem permissão para usar esse comando.",
                color = 0x5900FF
            )
            await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
            await ctx.message.delete() # apaga a mensagem do autor do comando.

    # ADD ROLE
    @commands.hybrid_command(name = 'addrole')
    @commands.check(AllowedChannels)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):

        # Verifica se o usuário que usou o comando tem permissão.
        ctx_member = ctx.guild.get_member(ctx.author.id)
        if ctx_member.guild_permissions.administrator:

            # membro
            member = ctx.guild.get_member(member.id)
            get_roles = member.roles
            role_names = [role.name for role in get_roles]
            role = ctx.guild.get_role(role.id)

            if role.name in role_names:
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"O membro {member} já tem o cargo de {role}.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

            else:
                await member.add_roles(role)
                embed = discord.Embed(
                    title = "`✅「 comando finalizado! 」✅`",
                    description = f"Você adicionou o cargo de {role} para o membro {member}.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

        # Usuário não tem permissão.
        else:
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Você não tem permissão para usar esse comando.",
                color = 0x5900FF
            )
            await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
            await ctx.message.delete() # apaga a mensagem do autor do comando.

    # KICK
    @commands.hybrid_command(name = 'kick')
    @commands.check(AllowedChannels)
    async def kick(self, ctx, member: discord.Member, motivo):

        # Verifica se o usuário que usou o comando tem permissão.
        ctx_member = ctx.guild.get_member(ctx.author.id)
        if ctx_member.guild_permissions.administrator:

            try:
                await member.kick()
                embed = discord.Embed(
                    title = "`✅「 comando finalizado! 」✅`",
                    description = f"`「 {ctx.author.name} 」` expulsou o membro `「 {member} 」` do servidor.",
                    color = 0x5900FF
                )
                embed.add_field (
                    name = "Motivo:",
                    value = motivo,
                    inline = True
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
            except:
                embed = discord.Embed(
                    title = "`❌「 houve um problema! 」❌`",
                    description = f"Não é possível expulsar o membro `「 {member} 」` por que ele tem um cargo mais alto no servidor.",
                    color = 0x5900FF
                )
                await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)

        # Usuário não tem permissão.
        else:
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = f"Você não tem permissão para usar esse comando.",
                color = 0x5900FF
            )
            await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
            await ctx.message.delete() # apaga a mensagem do autor do comando.

async def setup(bot):
    await bot.add_cog(Admin(bot))