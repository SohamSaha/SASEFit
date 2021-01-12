import discord
import os
from discord.ext import commands
import commands as logic

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
  logic.checkTime()
  print ('Bot is ready')

client.run(os.environ['SASEFIT_TOKEN'])