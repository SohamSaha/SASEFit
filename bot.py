import discord
import os
from discord.ext.tasks import loop
from discord.ext import commands
from datetime import datetime

#Set the command prefix for any future extensions and declare environment variables and other global variables
bot = commands.Bot(command_prefix='$')
emojis = ['\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']
SASEFIT_TOKEN = os.environ['SASEFIT_TOKEN']

@bot.event
async def on_ready():
  print ('Bot is ready')

@loop(count=None, seconds=1)  #Will run forever every second
async def check_calendar():
  channel = bot.get_channel(797665110629548052)

  #Get the date and time from the Heroku system and format it appropriately
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print (current_time)
  #As the  Heroku system uses the GMT+0 timezone, a 8 hour offset is required
  if (current_time == '04:00:00'):
    message = await channel.send('Did you achieve your goals?')
    for emoji in emojis:
      await message.add_reaction(emoji)

@check_calendar.before_loop
async def before_check_calendar():
    await bot.wait_until_ready()  # Wait until bot is ready

check_calendar.start()
bot.run(SASEFIT_TOKEN)