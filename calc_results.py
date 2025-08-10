#!/usr/bin/python3
import os
import sys
from datetime import datetime

NOTES_FILE = os.path.join(os.curdir, 'progress.md')
NOTES_FILE_TMP = f"{NOTES_FILE}.tmp"

records = {}
sum_cnt = 0
first_day = None
source_data = []
ignore_lines = [
    "всего часов учёбы",
    "всего прошло"
]
rep_str = "Статистика обучения"
rep_cur_indx = 0
rep_indx = 0
try:
    with open(NOTES_FILE, 'r') as fd_read:
        while st := fd_read.readline():
            source_data.append(st)
            if st.find(rep_str) == -1 and rep_indx == 0:
                rep_cur_indx += 1
            else:
                rep_indx = rep_cur_indx
            for ign in ignore_lines:
                if st.find(ign) != -1:
                    source_data.pop()
                    break
            try:
                _, date, time, cnt, _ = st.split('|')
                cnt = int(cnt)
                sum_cnt += cnt
                records[date] = cnt
                if first_day is None:
                    first_day = date
            except ValueError:
                pass
except FileNotFoundError as fnfe:
    print(f"Не могу открыть файл {NOTES_FILE}! Ошибка: {fnfe}")
    sys.exit(1)


total_learning = (
    f"- всего часов учёбы: {sum_cnt}ч за {len(records.keys())} дней: "
    f"{sum_cnt / len(records.keys()):.2f} часов/день."
)

s_d, s_m, s_y = list(map(int, first_day.split('.')))
s_y += 2000
d_from = datetime(year=s_y, month=s_m, day=s_d)
d_today = datetime.today()
d_passed = (d_today - d_from).days
total_passed = f"- всего прошло {d_passed} дней, а это {sum_cnt / d_passed:.2f}ч/день в среднем за весь период."

try:
    with open(NOTES_FILE_TMP, "wt", encoding="utf-8") as fd_write:
        fd_write.writelines(source_data[:rep_indx + 1])
        fd_write.write(total_learning + "\n")
        fd_write.write(total_passed + "\n")
        fd_write.writelines(source_data[rep_indx + 1:])
except FileNotFoundError as fnte:
    print(f"Не могу открыть файл {NOTES_FILE_TMP} на запись! Ошибка: {fnte}")
    sys.exit(1)

os.rename(NOTES_FILE_TMP, NOTES_FILE)

print(total_learning, total_passed, sep="\n")
