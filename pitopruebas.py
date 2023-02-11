import discord
import pytz

from Usuario import User
from dbusers import dbusers
import pytz

##CONSTANTES
guild_id = 630135300131127320
users_path = 'database.db'
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
dbu = dbusers(users_path)

@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(f'[{timestamp(ctx.created_at)}] {ctx.author}: {ctx.content}')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

#SLASH COMMANDS que estamos probando

@bot.slash_command(guild_ids=[guild_id])
async def pito(ctx: discord.ApplicationContext):
    await ctx.respond("Piii!") 
    
    user = User(ctx.author.id, ctx.author.name)
    dbu.insertar_usuario(user)

# #PRINTS IN CONSOLE ALL MESSAGES. JUST FOR DEBUG
@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(f'[{timestamp(ctx.created_at)}] {ctx.author}: {ctx.content}')

def timestamp(dt): 
    #CONVIERTE una variable de tipo datetime.datetime 
    #en un string con formato dd-mm-yy HH:MM:SS.
    spain_tz = pytz.timezone('Europe/Madrid')
    dt_tz = dt.astimezone(spain_tz)
    timestamp = dt_tz.strftime('%d-%m-%y %H:%M:%S')
    return timestamp

##SAFE TOKEN & RUN
f = open("token", "r")
token = f.read()
bot.run(token)
