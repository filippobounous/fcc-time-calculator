def add_time(start, duration, day = None):

  if start.split(' ')[1] == 'AM':
    start_hour = int(start.split(':')[0])
  else:
    start_hour = (int(start.split(':')[0]) + 12) % 24
  
  start_minute = int(start.split(':')[1][:2])
  
  duration_hour = int(duration.split(':')[0])
  duration_minute = int(duration.split(':')[1])
  days_of_week = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

  new_minute = (start_minute + duration_minute) % 60
  new_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 24
  new_days = (start_hour + duration_hour + (start_minute + duration_minute) // 60) // 24
  
  if new_hour == 0:
    hour = 12
    period = 'AM'
  elif new_hour >= 1 and new_hour < 12:
    hour = new_hour
    period = 'AM'
  elif new_hour == 12:
    hour = new_hour
    period = 'PM'
  else:
    hour = new_hour - 12
    period = 'PM'
    
  if new_days == 0:
    days = ''
  elif new_days == 1:
    days = ' (next day)'
  else:
    days = ' (' + str(new_days) + ' days later)'
  
  if day is not None:
    day = day.lower()
    day_of_week = days_of_week[day]
    new_day_of_week = (day_of_week + new_days) % 7
    new_day = list(days_of_week.keys())[list(days_of_week.values()).index(new_day_of_week)]
    days = ', ' + new_day.capitalize() + days

  hour_str = str(hour)

  if new_minute < 10:
    minute_str = '0'+str(new_minute)
  else:
    minute_str = str(new_minute)
  
  print(hour_str + ':' + minute_str + ' ' + period + days)
  return hour_str + ':' + minute_str + ' ' + period + days