import json
import os


def load_data(filepath):
    if not os.path.exists(filepath) or os.path.isdir(filepath):
        return None

    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print (json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    while True:
        filepath = input('Введите путь к файлу: ')
        data = load_data(filepath)

        if data is not None:
            pretty_print_json(data)
            break

        else:
            print('Некорректный адрес файла, повторите ввод')
