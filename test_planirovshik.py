import os
import unittest

import planirovshik

TASKS = [
    ["1", "Прочитать главу по Git", "1", "готово"],
    ["2", "Сделать рейтинговую работу", "1", "в работе"],
    ["3", "Сдать отчёт по практике", "1", "надо сделать"],
    ["4", "Купить тетради", "", "надо сделать"],
]


class TestPlanirovshik(unittest.TestCase):
    def test_week_result(self):
        """Итоги недели по статусам"""
        result = planirovshik.week_result(TASKS, "1")
        self.assertEqual(result, {"надо сделать": 1, "в работе": 1, "готово": 1})

    def test_task_without_week(self):
        """Задача без недели не попадает в итоги"""
        result = planirovshik.week_result(TASKS, "2")
        self.assertEqual(sum(result.values()), 0)

    def test_save_and_load(self):
        """Сохранение в файл и чтение из файла"""
        planirovshik.save("test_zadachi.csv", TASKS)
        self.assertEqual(planirovshik.load("test_zadachi.csv"), TASKS)
        os.remove("test_zadachi.csv")

    def test_load_missing_file(self):
        """Чтение несуществующего файла даёт пустой список"""
        self.assertEqual(planirovshik.load("net_takogo_faila.csv"), [])


if __name__ == "__main__":
    unittest.main()
