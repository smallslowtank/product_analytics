from queries import *

# def convert_unix_time(ts):
#     return datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

# create_tables()

print('---***---')
ar = select_count()
print(f"Всего запросов в базе: {ar}")

print('---***---')
start = select_min_date()
stop = select_max_date()
print(f"Начало периода: {start}\nКонец периода: {stop}")
print("Местное время хоста, на котором выполняется скрипт, в БД дата храниться в UTC.")

print('---***---')
print(f'Количество запросов ТОЛЬКО с "ютуб":')
res = select_only_youtube()
for i in res:
    print(i)

print('---***---')
res = select_only_youtube_touch()
print(f'Проверка. На тачах: {res}')

print('---***---')
print(f'Количество запросов НА ТЕМУ "ютуб":')
res = select_all_youtube()
for i in res:
    print(i)

print('---***---')
res = select_all_youtube_desktop()
print(f'Проверка. На десктопах: {res}')

print('---***---')
print("Топ 10 запросов на тачах:")
res = top10_request_touch()
for i in res:
    print(i)

print('---***---')
print("Топ 10 запросов на десктопах:")
res = top10_request_desktop()
for i in res:
    print(i)



print('---***---')
