# Будет полезно при парсинге различных данных и последующего сохранения их. Как идея - ежедневное получение цены токена, запись в CSV файл и анализ изменения стоимости за неделю/месяц/год.
#
# Библиотеку json устанавливать не нужно, она уже встроена в пакет Python

import json

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')