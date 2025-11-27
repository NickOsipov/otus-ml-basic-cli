"""
Script: main.py
Description: Простой пайплайн для чтения данных, применения линейной модели и записи результатов.
"""

import os

from src.data import read_data, write_data
from src.model import LinearModel


def main() -> None:
    """
    Основная функция для выполнения пайплайна.
    """

    # Пути к файлам
    input_file = os.path.join("data", "input", "dataset.csv")
    output_file = os.path.join("data", "output", "results.csv")

    # Чтение данных
    data = read_data(input_file)

    # Инициализация модели
    model = LinearModel(weight=2, intercept=5)

    # Предсказание результатов
    predictions = model.predict(data)

    # Запись результатов
    write_data(output_file, predictions)


if __name__ == "__main__":
    main()
