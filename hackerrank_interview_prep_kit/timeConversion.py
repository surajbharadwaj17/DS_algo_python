"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.


"""

def timeConversion(s):
    time_period = s[-2:]
    time = s[:-2].split(':')
    hour, min, sec = time[0], time[1], time[2]
    
    if time_period == 'PM':
        hour = str(int(hour)+12)
    
    print(hour,time_period)

    if (int(hour) == 24 and time_period == 'PM'):
        hour = '12'

    if (time_period == 'AM' and int(hour) == 12):
        hour = '00'

    print(f"{hour}:{min}:{sec}")


s = '12:45:54PM'
timeConversion(s)


