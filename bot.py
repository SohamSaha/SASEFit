import os
import json
import discord
import helper as helper
from datetime import datetime
from discord.ext import commands
from discord.ext.tasks import loop

#Set the command prefix for any future extensions and declare environment variables and other global variables
bot = commands.Bot(command_prefix='$')
emojis = ['\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']
SASEFIT_TOKEN = os.environ['SASEFIT_TOKEN']
youtube_channel = 'UCCgLoMYIyP0U56dEhEL1wXQ'

@bot.event #Verify the bot is ready
async def on_ready():
  print ('Bot is ready')
  
@loop(count=None, seconds=1)  #Will run forever every second
async def check_calendar():
  channel = bot.get_channel(797665110629548052)

  #Get the date and time from the Heroku system and format it appropriately
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  current_day = now.strftime("%A")

  #As the  Heroku system uses the GMT+0 timezone, a 8 hour offset is required
  if (current_time == '04:00:00'): #Send a check-in every day at 8 PM PST to hold people accountable
    check_in_message = await channel.send('Did you achieve your goals?')
    for emoji in emojis:
      await check_in_message.add_reaction(emoji)

    with open('check_ins.json','r+') as json_file:
      data = json.load(json_file)
    if (check_in_message.id not in data):
      data[check_in_message.id]=[{}]  
    with open('check_ins.json','w') as json_file:
      json_file.write(json.dumps(data))

  elif (current_time == '17:00:00') and (current_day == 'Sunday'): #Send a new video every Sunday at 9 AM PST to help people out
    suggestion_message = await channel.send(helper.get_channel_videos(youtube_channel))
    with open('check_ins.json','r+') as json_file:
      data = json.load(json_file)
    total_days=len(data.keys())
    message = await channel.send('out of ' + total_days + ' days this week, you achieved your goal for 3 of them')

@check_calendar.before_loop
async def before_check_calendar():
    await bot.wait_until_ready()  # Wait until bot is ready

@bot.event
async def on_raw_reaction_add(payload):
  if payload.guild_id is None:
    return  # Reaction is on a private message
  with open('check_ins.json','r+') as json_file:
    data = json.load(json_file)
  if (payload.message_id in data) and (payload.channel_id == 797665110629548052):
    if (not payload.member.bot) and (str(payload.emoji) == '👍'):
      with open('check_ins.json','r+') as json_file:
        data = json.load(json_file)
      if (str(payload.message_id) not in data):
        data[str(payload.message_id)][0][payload.member]='1'  
      with open('check_ins.json','w') as json_file:
        json_file.write(json.dumps(data))
    
check_calendar.start()
bot.run(SASEFIT_TOKEN)