"""
Script: main.py
Description: Простой пайплайн для чтения данных, применения линейной модели и записи результатов.
"""

from argparse import ArgumentParser
import os

from loguru import logger

from src.data import read_data, write_data
from src.model import LinearModel


def main() -> None:
    """
    Основная функция для выполнения пайплайна.
    """

    logger.info(f"Старт скрипта {__file__}")
    logger.info("Создание аргументов командной строки")

    # Создание аргументов командной строки
    parser = ArgumentParser(description="Простой пайплайн для линейной модели.")
    parser.add_argument(
        "--input_file",
        type=str,
        default="dataset.csv",
        help="Путь к входному файлу CSV.",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="results.csv",
        help="Путь к выходному файлу CSV.",
    )
    parser.add_argument(
        "--weight",
        type=float,
        default=2.0,
        help="Коэффициент наклона линейной модели.",
    )
    parser.add_argument(
        "--intercept",
        type=float,
        default=5.0,
        help="Свободный член линейной модели.",
    )
    args = parser.parse_args()

    input_filename = args.input_file
    output_filename = args.output_file
    weight = args.weight
    intercept = args.intercept

    # Пути к файлам
    input_file = os.path.join("data", "input", input_filename)
    output_file = os.path.join("data", "output", output_filename)

    # Чтение данных
    logger.info(f"Чтение данных из файла: {input_file}")
    data = read_data(input_file)

    # Инициализация модели
    logger.info("Инициализация линейной модели")
    logger.debug(f"Параметры модели: weight={weight}, intercept={intercept}")
    model = LinearModel(weight=weight, intercept=intercept)

    # Предсказание результатов
    logger.info("Выполнение предсказаний")
    predictions = model.predict(data)

    # Запись результатов
    logger.info(f"Запись результатов в файл: {output_file}")
    write_data(output_file, predictions)

    logger.info("Завершение работы скрипта")

if __name__ == "__main__":
    main()
