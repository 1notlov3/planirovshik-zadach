import csv
import os
from datetime import date

TASKS_FILE = "zadachi.csv"
WEEKS_FILE = "nedeli.csv"
STATUSES = ["надо сделать", "в работе", "готово"]


def load(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, encoding="utf-8") as f:
        return list(csv.reader(f, delimiter=";"))


def save(file_name, rows):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";").writerows(rows)


def add_task(tasks):
    title = input("Название задачи: ").strip()
    if title == "":
        print("Название не может быть пустым")
        return
    number = str(len(tasks) + 1)
    tasks.append([number, title, "", STATUSES[0]])
    save(TASKS_FILE, tasks)
    print("Задача", number, "добавлена в общий список")


def show_tasks(tasks):
    if not tasks:
        print("Задач пока нет")
        return
    for number, title, week, status in tasks:
        week_text = "неделя " + week if week else "без недели"
        print(number, title, "|", week_text, "|", status)


def start_week(weeks):
    number = str(len(weeks) + 1)
    weeks.append([number, date.today().strftime("%d.%m.%Y")])
    save(WEEKS_FILE, weeks)
    print("Начата неделя", number)


def find_task(tasks):
    number = input("Номер задачи: ")
    for task in tasks:
        if task[0] == number:
            return task
    print("Нет такой задачи")
    return None


def take_to_week(tasks, weeks):
    if not weeks:
        print("Сначала начните неделю")
        return
    task = find_task(tasks)
    if task and task[3] == "готово":
        print("Задача уже выполнена")
    elif task:
        task[2] = weeks[-1][0]
        save(TASKS_FILE, tasks)
        print("Задача взята в неделю", task[2])


def change_status(tasks):
    task = find_task(tasks)
    if not task:
        return
    for number, status in enumerate(STATUSES, 1):
        print(number, status)
    choice = input("Новый статус: ")
    if choice not in ("1", "2", "3"):
        print("Нет такого статуса")
        return
    task[3] = STATUSES[int(choice) - 1]
    save(TASKS_FILE, tasks)
    print("Статус изменён")


def week_result(tasks, week):
    result = {status: 0 for status in STATUSES}
    for task in tasks:
        if task[2] == week:
            result[task[3]] += 1
    return result


def show_week_result(tasks, weeks):
    if not weeks:
        print("Недель пока нет")
        return
    week, start = weeks[-1]
    result = week_result(tasks, week)
    print("Неделя", week, "с", start)
    for status, count in result.items():
        print(status, "-", count)
    total = sum(result.values())
    if total > 0:
        # доля выполненных задач в процентах
        print("Выполнено:", round(result["готово"] * 100 / total), "%")


def main():
    tasks = load(TASKS_FILE)
    weeks = load(WEEKS_FILE)
    while True:
        print()
        print("1 - Добавить задачу в общий список")
        print("2 - Показать общий список")
        print("3 - Начать новую неделю")
        print("4 - Взять задачу в неделю")
        print("5 - Изменить статус задачи")
        print("6 - Итоги недели")
        print("0 - Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            start_week(weeks)
        elif choice == "4":
            take_to_week(tasks, weeks)
        elif choice == "5":
            change_status(tasks)
        elif choice == "6":
            show_week_result(tasks, weeks)
        elif choice == "0":
            break
        else:
            print("Нет такого пункта")


if __name__ == "__main__":
    main()
