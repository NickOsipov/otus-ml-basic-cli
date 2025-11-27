# OTUS. ML-Basic. Практика CLI 

Простое CLI-приложение для применения линейной модели к данным.

## Описание проекта

Проект реализует простой пайплайн машинного обучения с использованием линейной модели вида `y = weight * x + intercept`. Приложение читает входные данные из CSV-файла, применяет к ним линейную трансформацию и записывает результаты в выходной CSV-файл.

## Структура проекта

```
otus-ml-basic-cli/
├── data/
│   ├── input/           # Директория для входных данных
│   │   └── dataset.csv
│   ├── output/          # Директория для результатов
│   └── test.csv
├── notebooks/           # Jupyter notebooks для экспериментов
│   └── work.ipynb
├── src/                 # Исходный код приложения
│   ├── main.py          # Основной скрипт с CLI
│   ├── model.py         # Класс линейной модели
│   └── data.py          # Функции для работы с данными
├── tests/               # Юнит-тесты
│   ├── test_model.py
│   └── test_data.py
├── pyproject.toml       # Конфигурация проекта
├── requirements.txt     # Зависимости проекта
└── README.md
```

## Требования

- Python 3.11.4

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd otus-ml-basic-cli
```

2. Создайте виртуальное окружение:
```bash
uv sync
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows
```

## Использование

### Базовое использование

Запуск с параметрами по умолчанию:
```bash
python -m src.main
```

Это прочитает данные из `data/input/dataset.csv`, применит модель с параметрами `weight=2.0` и `intercept=5.0`, и сохранит результаты в `data/output/results.csv`.

### Использование с пользовательскими параметрами

```bash
python -m src.main \
  --input_file dataset.csv \
  --output_file predictions.csv \
  --weight 3.5 \
  --intercept 1.2
```

### Параметры командной строки

- `--input_file`: Имя входного CSV-файла (по умолчанию: `dataset.csv`)
- `--output_file`: Имя выходного CSV-файла (по умолчанию: `results.csv`)
- `--weight`: Коэффициент наклона линейной модели (по умолчанию: `2.0`)
- `--intercept`: Свободный член линейной модели (по умолчанию: `5.0`)

### Примеры

Применить модель с коэффициентом 10 и сдвигом 0:
```bash
python -m src.main --weight 10 --intercept 0
```

Использовать другой входной файл:
```bash
python -m src.main --input_file custom_data.csv --output_file custom_results.csv
```

## Формат данных

### Входной файл

CSV-файл с одним столбцом числовых значений:
```
1.0
2.5
3.7
4.2
```

### Выходной файл

CSV-файл с предсказанными значениями:
```
7.0
10.0
12.4
13.4
```

## Модули

### src/model.py

Содержит класс `LinearModel` для выполнения линейных преобразований.

```python
model = LinearModel(weight=2.0, intercept=5.0)
predictions = model.predict([1, 2, 3])
# Результат: [7, 9, 11]
```

### src/data.py

Предоставляет функции для чтения и записи данных:
- `read_data(file_path)`: Читает числовые данные из CSV-файла
- `write_data(file_path, data)`: Записывает данные в CSV-файл

### src/main.py

Основной скрипт, который объединяет все компоненты в единый пайплайн.

## Тестирование

Запуск всех тестов:
```bash
pytest
```

Запуск тестов с покрытием кода:
```bash
pytest --cov=src tests/
```

Запуск конкретного теста:
```bash
pytest tests/test_model.py
```

## Разработка

### Форматирование кода

Проект использует `black` для форматирования кода:
```bash
black src/ tests/
```

### Линтинг

Проверка кода с помощью `pylint`:
```bash
pylint src/ tests/
```

## Лицензия

Проект создан в образовательных целях для курса OTUS.

## Автор

[Nick Osipov](https:/t.me/NickOsipov)
