import discord
from discord import app_commands
import pytz
# from discord.ext.commands import Bot
# from discord.ext import commands

guild_id = 630135300131127320

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = guild_id))#guild = discord.Object(id = guild_id)
            self.synced = True
        print(f'Logged in as {self.user}')



client = aclient()

tree = app_commands.CommandTree(client)
@tree.command(name="test", description="testing", guild = discord.Object(id = guild_id) )
async def test(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello {name}! I was made with Discord.py!')
# intents = discord.Intents.default()
# intents.message_content = True

# bot = Bot(command_prefix = "/", intents = intents)

spain_tz = pytz.timezone('Europe/Madrid')

# #PRINTS IN CONSOLE ALL MESSAGES. JUST FOR DEBUG
@client.event
async def on_message(interaction: discord.Interaction):

    if interaction.author == client.user:
        return
    dt = interaction.created_at
    dt_tz = dt.astimezone(spain_tz)
    timestamp = dt_tz.strftime('%d-%m-%y %H:%M:%S')
    print(f'[{timestamp}] {interaction.author}: {interaction}')


# @bot.slash_command()
# async def test(ctx):
#     await ctx.reply("Piiii")

f = open("token", "r")
token = f.read()
# bot.run(token)
client.run(token)