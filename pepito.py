import discord
from discord.ui import Button, View, Select
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

#SLASH COMMANDS



# CREAR CLASE VIEW

#EJEMPLO DE MODAL Y DE MENSAJE TIPO EMBED
class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short Input"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

@bot.slash_command(guild_ids=[guild_id])
async def modal(ctx: discord.ApplicationContext):
    """Shows an example of a modal dialog being invoked from a slash command."""
    modal = MyModal(title="Modal via Slash Command")
    await ctx.send_modal(modal)
  
""" 
@bot.slash_command(guild_ids=[guild_id])
async def inscribirme(ctx: discord.ApplicationContext):
    print() """


@bot.slash_command(guild_ids=[guild_id])
async def pito(ctx: discord.ApplicationContext):
    await ctx.respond("Piii!") 

@bot.slash_command(guild_ids = [guild_id])
async def usuario(ctx: discord.ApplicationContext):
    user = User(ctx.author.id, ctx.author.name)
    dbu.insertar_usuario(usuario = user)
    await ctx.respond(user.toString())

@bot.slash_command(guild_ids = [guild_id])
async def dbuselect(ctx: discord.ApplicationContext): 
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
