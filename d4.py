from datetime import datetime, timedelta
from itertools import combinations
from common import load_day_data
from parse import parse
from collections import namedtuple, defaultdict
from pprint import pprint

data = load_day_data(4)

def get_datetime(line):
    stamp = line[1:17]
    return datetime.strptime(stamp,'%Y-%m-%d %H:%M')

# def parse_input_line(line):
#     """
#     [1518-07-18 23:57] Guard #157 begins shift
#     [1518-04-18 00:44] falls asleep / wakes up
#     """
#     guard, asleep, awake = None, None, None
#     stamp = parse('{:14}{:2}{}, line).fixed[1]
#     if 'Guard' in line:
#         guard = parse("[{}] Guard #{:d} begins shift", line).fixed[-1]
#     else:
#         pass
#     return stamp, guard, asleep, awake

guards = dict()

current_guard = None


def is_guard_line(line):
    return 'Guard' in line

def is_sleep_line(line):
    return 'falls' in line

def is_awake_line(line):
    return 'wake' in line

def parse_guard_number(line):
    return int(line.split("#")[1].split(' ')[0])

def parse_minute(line):
    return get_datetime(line).minute
last_guard = -1

history  = defaultdict(list)

for line in sorted(data, key=get_datetime):
    # time, guard, asleep, awake = parse_input_line()
    if is_guard_line(line):
        last_guard = parse_guard_number(line), (get_datetime(line) + timedelta(hours=12)).date()
        history[last_guard].append(( 0, 'awake' ))

    if is_awake_line(line):
        history[last_guard].append((parse_minute(line), 'awake'))
    
    if is_sleep_line(line):
        history[last_guard].append((parse_minute(line), 'sleep'))

# with open('sorted_d4', 'w') as f:
#     f.writelines(sorted(data, key=get_datetime))


# pprint(dict(history))

def get_sleep_minutes(schedule):
    total = 0
    last_state = 'awake'

    lkp = dict(schedule)

    for i in range(60):
        last_state = lkp.get(i, last_state)
        if last_state == 'sleep':
            total += 1

    return total



class Shift:
    def __init__(self, k, v):
        self.guard = k[0]
        self.date = k[1]
        self.schedule = v
        self.sleep_minutes = get_sleep_minutes(self.schedule)
        self.lkp = dict(self.schedule)
    
    def is_asleep(self, minute):
        while minute >= 0:
            q = self.lkp.get(minute, None)
            if q is not None:
                return q == 'sleep'
            minute -= 1
        return False

    def __repr__(self):
        return f"{self.guard} {self.date} {self.sleep_minutes}"

shifts = sorted((Shift(k,v) for k,v in history.items()), key=lambda x: x.sleep_minutes, reverse=True)

dd2 = defaultdict(lambda: 0)

for s in shifts:
    dd2[s.guard] += s.sleep_minutes

q = sorted(((g, sm) for g, sm in dd2.items()), key=lambda x: x[1], reverse = True)[0]

print(q)

sleepy_guards_shifts = [shift for shift in shifts if shift.guard == q[0]]

common_minutes = defaultdict(lambda: 0)

for minute in range(60):
    for shift in sleepy_guards_shifts:
        if shift.is_asleep(minute):
            common_minutes[minute] += 1

pprint(dict(common_minutes))

mins = sorted(((minute,times) for minute, times in common_minutes.items()), key= lambda x: x[1], reverse=True)[0][0]

print(mins * q[0])  # Answer to part one.
