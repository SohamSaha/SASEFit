import discord
import os
from discord.ext import commands
import commands as logic

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready(ctx):
  await ctx.send('hola')
  if(logic.checkTime()):
    await ctx.send('hi')
  
  print ('Bot is ready')

client.run(os.environ['SASEFIT_TOKEN'])