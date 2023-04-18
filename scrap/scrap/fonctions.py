def convert_to_minutes(time):
    if time and 'h' in time and 'm' in time:
        hours, minutes = time.split('h ')
        minutes = minutes.rstrip('m')
        duration= int(hours) * 60 + int(minutes)
    elif time and 'h' in time :
        hours=time.rstrip('h')
        duration = int(hours)*60
    elif time and 'm' in time:
        minute = time.rstrip('m')
        duration = int(minute)
    else :
        duration = None
    return duration

