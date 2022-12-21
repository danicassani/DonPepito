import discord

from discord.ext import commands
from Usuario import User
from dbusers import dbusers
import pytz

##CONSTANTES
guild_id = 630135300131127320
users_path = 'database.db'
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)


# dbu.crear_tabla_usuarios(users_path)

@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(f'[{timestamp(ctx.created_at)}] {ctx.author}: {ctx.content}')



#SISTEMAS INICIALIZADOS
dbu = dbusers(users_path)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

#SLASH COMMANDS

###BOTONES
class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

@bot.slash_command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button
####

@bot.slash_command(guild_ids=[guild_id])
async def pito(ctx: discord.ApplicationContext):
    await ctx.respond("Piii!") 

@bot.slash_command(guild_ids = [guild_id])
async def usuario(ctx: discord.ApplicationContext):
    user = User(ctx.author.id, ctx.author.name)
    dbu.insertar_usuario(usuario = user)
    await ctx.respond(user.toString());

@bot.slash_command(guild_ids = [guild_id])
async def select(ctx: discord.ApplicationContext): 
    dbu.seleccionar_usuario(ctx.author.id)
    await ctx.respond("selected")


##FUNCIONES PROPIAS
def timestamp(dt): 
    #CONVIERTE una variable de tipo datetime.datetime 
    #en un string con formato dd-mm-yy HH:MM:SS.
    spain_tz = pytz.timezone('Europe/Madrid')
    dt_tz = dt.astimezone(spain_tz)
    timestamp = dt_tz.strftime('%d-%m-%y %H:%M:%S')
    return timestamp

# #PRINTS IN CONSOLE ALL MESSAGES. JUST FOR DEBUG
@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(f'[{timestamp(ctx.created_at)}] {ctx.author}: {ctx.content}')

##SAFE TOKEN & RUN
f = open("token", "r")
token = f.read()
bot.run(token)
