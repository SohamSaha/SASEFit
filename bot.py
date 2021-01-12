import discord
import os
from discord.ext import commands
from datetime import datetime
import threading

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready(ctx):
  print ('Bot is ready')


def checkTime():
  threading.Timer(1, checkTime).start()

  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  # print ("Current Time =", current_time)

  if (current_time == '05:30:00'):
    print('it time')
  else:
    print('iit not time')

client.run(os.environ['SASEFIT_TOKEN'])