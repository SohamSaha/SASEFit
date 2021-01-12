import discord
import os
from discord.ext import commands
from datetime import datetime
import threading

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
  print ('Bot is ready')
  checkTime()


########################################################################################################################################################################
#   Helper functions that are not any commands/events but are utilized in other ways                                                                                   #
########################################################################################################################################################################

def checkTime(ctx):
  #Start a thread to check the time every second
  threading.Timer(1, checkTime).start()

  #acquire the date and time and format the time in Hours: Minutes: Seconds
  #Note: The time is given in GMT+0 timezone
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  
  #Check if the time is correct and send a message appropriately
  if (current_time == '06:50:00'):
    await ctx.send('it time')
    print('it time')

client.run(os.environ['SASEFIT_TOKEN'])