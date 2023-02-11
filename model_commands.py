import discord

from discord.ui import Button, View, Select

###BOTONES
async def botones_id(text:str):
  print(text)

boton1 = Button(label="Primary", style=discord.ButtonStyle.primary)
async def boton1_callback(interaction: discord.Interaction):
  await interaction.response.send_message("Botón primario!")
  return "Botón primario!"
boton1.callback = boton1_callback

boton2 = Button(label="Secondary", style=discord.ButtonStyle.secondary)
async def boton2_callback(interaction: discord.Interaction):
  
  return "Botón secundario!" 
  #await interaction.response.send_message("Botón secundario!")
boton2.callback = boton2_callback

boton3 = Button(label="Danger", style=discord.ButtonStyle.danger)
async def boton3_callback(interaction: discord.Interaction):
  return "Cuidado!!"
   #await interaction.response.send_message("CUIDADO!!")
boton3.callback = boton3_callback

@bot.slash_command()
async def button(ctx):  
    view = View(boton1, boton2, boton3)
    await ctx.respond("Theese are some buttons!", view=view) # Send a message with our View class that contains the button
###/BOTONES

###SELECTER
async def select_tortilla(interaction: discord.Interaction):
    seleccion = interaction.data["values"][0]
    await interaction.response.send_message("Tortilla seleccionada. " + seleccion)

@bot.slash_command() # Create a slash command
async def tortilla(ctx: discord.ApplicationContext):
    seleccionable = Select(placeholder="Selecciona una opción:", options=[
    discord.SelectOption(label="Con cebolla", emoji="👍",description="La opción correcta."),
    discord.SelectOption(label="Sin cebolla", emoji="👎",description="Eres un monstruo.") ])
    view = View(seleccionable)
    seleccionable.callback = select_tortilla
    await ctx.respond("La tortilla, ¿con cebolla o sin cebolla?", view = view)
###/SELECTER