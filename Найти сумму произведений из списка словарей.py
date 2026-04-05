import json

def task() -> float: #объявляем функцию, которая возвращает число с плавающей точкой (float)
    with open("input.json") as f: #открываем файл, он сам закроется после прекращения работы
        data = json.load(f) #превращаем JSON в список словарей
    return round(sum(i["score"] * i["weight"] for i in data), 3) #каждый элемент i в списке data умножаем score на weigh, потом суммируем и округляем до 3 знаков

print(task()) #вызываем функцию task и выводим результат