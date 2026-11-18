import csv
import os
from datetime import date

TASKS_FILE = "zadachi.csv"
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


def main():
    tasks = load(TASKS_FILE)
    while True:
        print()
        print("1 - Добавить задачу в общий список")
        print("2 - Показать общий список")
        print("0 - Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "0":
            break
        else:
            print("Нет такого пункта")


if __name__ == "__main__":
    main()
