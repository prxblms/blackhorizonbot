from src.settings import *
from src.tasks import *

intents = discord.Intents.all() # Todas as interações.
bot = commands.Bot(command_prefix = prefix, intents = intents)
bot.remove_command('help') # Remove o (help) padrão.

@tasks.loop(minutes = 3) # Tarefa, música do status do bot.
async def ChangeMusicActivity():
    await MusicActivity(bot)

@bot.event
async def on_ready():
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "Xzhyan - Levantamento"))
    # AutoSendMessage.start()
    ChangeMusicActivity.start()
    os.system('cls && title After Dawn Bot')
    print(" BlackHorizon™ Bot online! ")
    try:
        synced = await bot.tree.sync()
        print(f" Slash Commands encontrados: {len(synced)}")
    except Exception as e:
        print(e)

async def loadcogs(): # Função para carregar as cogs/extensões do bot.
    print(" Carregando as extensões do bot... ")
    for cognames in os.listdir('./cogs'):
        if cognames.endswith('.py'):
            await bot.load_extension(f'cogs.{cognames[:-3]}')

async def main():
    await loadcogs()
    await bot.start(token)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    os.system('cls')
    print(" O Bot foi interrompido...")