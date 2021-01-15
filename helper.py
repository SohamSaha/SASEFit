import random
import os
from googleapiclient.discovery import build

api_key = os.environ['YOUTUBE_API_KEY']
youtube = build('youtube','v3', developerKey=api_key) #Build the Youtube object using the developer key from the environment


def get_channel_videos(channel_id):
  videos = []
  next_page_token=None

  #Loop through all the videos until no 'next page' is found which implies all videos have been found
  while True:
    vids = youtube.playlistItems().list(playlistId='UUCgLoMYIyP0U56dEhEL1wXQ', part='snippet',maxResults=1,pageToken=next_page_token).execute()

    #If the word 'workout' or 'Workout' is found in the title, assume it's a workout video and append to the final list
    if 'workout' in vids['items'][0]['snippet']['title'] or 'Workout' in vids['items'][0]['snippet']['title']:
      message = 'For this week, the suggested warmup/ workout is: ' + vids['items'][0]['snippet']['title'] + ' found at https://www.youtube.com/watch?v=' + vids['items'][0]['snippet']['resourceId']['videoId']
      videos+=[message]

    #Get the next page token to keep going and finding all the videos. Stop the loop if the last video is found
    next_page_token= vids.get('nextPageToken')
    if next_page_token is None:
      break
  
  #Return one random video
  videos_length=len(videos)
  return videos[random.randint(0,videos_length-1)]