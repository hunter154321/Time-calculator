def add_time(start_t, add_t, day = -1):
  split_start_t1, split_start_t2 = start_t.split(':')
  split_start_t2, am_pm = split_start_t2.split()
  split_add_t1, split_add_t2 = add_t.split(':')
  new_t1 = int(split_start_t1) + int(split_add_t1)
  new_t2 = int(split_start_t2) + int(split_add_t2)
  days_later = 0
  if day != -1:
    day = day_to_num(day)
  am_pm = ampm_to_num(am_pm)
  while new_t2 >= 60:
    new_t1 = new_t1 + 1
    new_t2 = new_t2 - 60
  while new_t1 >= 13:
    am_pm = am_pm + 1
    new_t1 = new_t1 - 12
  if new_t1 >= 12:
    am_pm = am_pm + 1
  while am_pm > 1 and day != -1:
    am_pm = am_pm - 2
    day = day + 1
    days_later = days_later + 1
  while day > 6 and day != -1:
    day = day - 7
  while am_pm > 1:
    am_pm = am_pm - 2
    days_later = days_later + 1
  if day > 0:  
    day = num_to_day(day)
  am_pm = num_to_ampm(am_pm)
  new_t1, new_t2 = str(new_t1), str(new_t2)
  if len(new_t2) < 2:
    new_t2 = '0' + new_t2
  if day != -1 and days_later > 1:
    days_later = ' (' + str(days_later) + " days later)"
    return(new_t1 + ':' + new_t2 + ' ' + am_pm + ', ' + day + days_later)
  elif day != -1 and days_later == 1:
    return(new_t1 + ':' + new_t2 + ' ' + am_pm + ', ' + day + ' (next day)')
  elif day != -1 and days_later == 0:
    return(new_t1 + ':' + new_t2 + ' ' + am_pm + ', ' + day)
  elif days_later > 1:
    days_later = ' (' + str(days_later) + " days later)"
    return(new_t1 + ':' + new_t2 + ' ' + am_pm + days_later)
  elif days_later == 1:
    return(new_t1 + ':' + new_t2 + ' ' + am_pm + ' (next day)')
  elif days_later == 0:
    return(new_t1 + ':' + new_t2 + ' ' + am_pm)

def ampm_to_num(x):
  if x == 'AM':
    return(0)
  else:
    return(1)

def num_to_ampm(x):
  if x == 0:
    return('AM')
  else:
    return('PM')

def day_to_num(x):
  x = x.lower()
  if x == 'sunday':
    return(0)
  if x == 'monday':
    return(1)
  if x == 'tuesday':
    return(2)
  if x == 'wednesday':
    return(3)
  if x == 'thursday':
    return(4)
  if x == 'friday':
    return(5)
  if x == 'saturday':
    return(6)

def num_to_day(x):
  if x == 0:
    return('Sunday')
  if x == 1:
    return('Monday')
  if x == 2:
    return('Tuesday')
  if x == 3:
    return('Wednesday')
  if x == 4:
    return('Thursday')
  if x == 5:
    return('Friday')
  if x == 6:
    return('Saturday')

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
