# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME):
    with open(INPUT_FILENAME, 'r') as csv_file:     # открываем файл
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader)      # назначаем заголовки
        data = []       # создаем список

        for row in csv_reader:
            dict = {header: value for header, value in zip(headers, row)} # создаем список c заголовками и значениями
            data.append(dict)       # добавляем в список

    json_data = json.dumps(data, indent=4)  # cериализуем python объект в строку формата JSON с дополнительными отступами

    with open(OUTPUT_FILENAME, 'w') as json_file: # открываем файл
        json_file.write(json_data)

def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
