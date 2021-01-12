from datetime import datetime
import threading

def checkTime():
  threading.Timer(1, checkTime).start()

  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  # print ("Current Time =", current_time)

  if (current_time == '05:27:00'):
    return True
  else:
    return False