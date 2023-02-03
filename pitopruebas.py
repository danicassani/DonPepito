import discord
import pytz
import wavelink

##CONSTANTES
guild_id = 630135300131127320
users_path = 'database.db'
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

async def connect_nodes():
  """Connect to our Lavalink nodes."""
  await bot.wait_until_ready() # wait until the bot is ready
  print("nodos conectados")

  await wavelink.NodePool.create_node(
    bot=bot,
    host='0.0.0.0',
    port=2333,
    password='youshallnotpass'
  ) # create a node

@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(f'[{timestamp(ctx.created_at)}] {ctx.author}: {ctx.content}')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    await connect_nodes() # connect to the server
    print("nodo conectado.")

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
  print(f"{node.identifier} is ready.") # print a message

async def connect_nodes():
  """Connect to our Lavalink nodes."""
  await bot.wait_until_ready() # wait until the bot is ready

  await wavelink.NodePool.create_node(
    bot=bot,
    host='lavalinkinc.ml',
    port=443,
    password='incognito',
    https=True
  ) # create a node

#SLASH COMMANDS
@bot.slash_command()
async def play(ctx: discord.ApplicationContext, search: str):
    vc = ctx.voice_client # define our voice client

    if not vc: # check if the bot is not in a voice channel
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) # connect to the voice channel
    if ctx.author.voice.channel.id != vc.channel.id: # check if the bot is not in the voice channel
        return await ctx.respond("You must be in the same voice channel as the bot.") # return an error message

    song = await wavelink.YouTubeTrack.search(query=search, return_first=True) # search for the song
    wavelink.YouTubeTrack.search
    print("SONG:",song)

    if not song: # check if the song is not found
        return await ctx.respond("No song found.") # return an error message

    await vc.play(song) # play the song
    await ctx.respond(f"Now playing: `{vc.source.title}`") # return a message

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
