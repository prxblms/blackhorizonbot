# Importações de outros arquivos python.
from src.settings import *

class Illegal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # DDOS
    @commands.hybrid_command(name = "ddos")
    @commands.check(AllowedChannels)
    @commands.has_any_role("security")
    async def ddos(self, ctx):

        ddos_list = [
            '> https://stresserr.ru `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://stresse.app `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://exoticstress.com `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://stresser.zone `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://inverse.best `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://str3ssed.co `free` `layer3/4` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.',
            '> https://github.com/epsylon/ufonet `free software` `layer7` \n> Não nos responsabilizamos pelo uso indevido dessas ferramentas. \n> We are not responsible for the misuse of these tools.'
        ]
        random_ddos = random.choice(ddos_list)
        await ctx.send(random_ddos, delete_after = 30)

    # IP INFO
    @commands.hybrid_command(name = 'ipinfo')
    @commands.check(AllowedChannels)
    @commands.has_any_role("security")
    async def ipinfo(self, ctx, ip):

        # Usa a API para pegar as informações do IP/Host.
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'fail':
            embed = discord.Embed(
                title = "`❌「 houve um problema! 」❌`",
                description = "O IP ou Host não foi digitado corretamente ou é inexistente.",
                color = 0x5900FF
            )
            await ctx.send(ctx.author.mention, embed = embed, delete_after = 10)
        else:
            embed = discord.Embed (
                title = "IP Lookup",
                description = f"`using http://ip-api.com`",
                color = 0x5900FF
            )
            embed.add_field(
                name = "• Informações do IP/Host:",
                value = f"`IP:` {data['query']}\n`Status:` {data['status']}\n`Country:` {data['country']}\n`Contry Code:` {data['countryCode']}\n`Region:` {data['region']}\n`Region Name:` {data['regionName']}\n`City:` {data['city']}\n`Zip:` {data['zip']}\n`Latitude:` {data['lat']}\n`Longitude:` {data['lon']}\n`Timezone:` {data['timezone']}\n`ISP:` {data['isp']}\n`ORG:` {data['org']}\n`AS:` {data['as']}",
                inline = True
            )
            await ctx.send(embed = embed, delete_after = 30)

async def setup(bot):
    await bot.add_cog(Illegal(bot))