import discord
import os
from discord.ext import commands
from datetime import datetime
import asyncio

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print ('Bot is ready')
  
@bot.command()
async def test(ctx):
  emojis= ['\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']
  message = await ctx.send("DID YOU ACHIEVE YOUR GOALS TODAY?")
  
  for emoji in emojis:
    await message.add_reaction(emoji)

async def checkTime():
  await bot.wait_until_ready()
  while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if (current_time == '04:00:00'):
      print('it time')
    else:
      pass
    await asyncio.sleep(1) 

bot.loop.create_task(checkTime())
bot.run(os.environ['SASEFIT_TOKEN'])