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


def checkTime():
  threading.Timer(1, checkTime).start()

  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  # print ("Current Time =", current_time)

  if (current_time == '06:40:00'):
    print('it time')

client.run(os.environ['SASEFIT_TOKEN'])