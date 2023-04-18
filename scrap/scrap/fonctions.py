def convert_to_minutes(time_str):
    hours, minutes = time_str.split('h ')
    minutes = minutes.rstrip('m')
    return int(hours) * 60 + int(minutes)
