from queries import *

# def convert_unix_time(ts):
#     return datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

# create_tables()

ar = select_count()
print(f"Всего запросов в базе: {ar}")

# n = int(input('Enter id: '))
# q = select_id(n)
# print(q)
# for i in q:
#     print(i)


sd = select_min_date()
print(f"Start_date: {sd}")
ed = select_max_date()
print(f"End_date: {ed}")

ytd = select_youtube_desktop()
print(f"Request 'ютуб' or 'Ютуб' on desktop: {ytd}")
ytt = select_youtube_touch()
print(f"Request 'ютуб' or 'Ютуб' on touch: {ytt}")
