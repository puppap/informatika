import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None: #объявляем функцию, которая ничего не возвращает
    with open(INPUT_FILENAME) as f: #открываем входной CSV файл
        lines = list(csv.DictReader(f)) #читаем CSV как список словарей (ключи будут названия столбцов, а значения - данные в этой строке)
    with open(OUTPUT_FILENAME, "w") as f: #открываем выходной JSON файл
        json.dump(lines, f, indent=4) #записываем список словарей lines в JSON файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")