"""
Module: data.py
Description: Модуль для работы с данными.
"""

from typing import List, Union
import csv

def read_data(file_path: str) -> List[Union[int, float]]:
    """
    Функция читает данные из файла CSV

    Parameters
    ----------
    file_path : str
        Путь к файлу CSV для чтения данных.
    
    Returns
    -------
    List[Union[int, float]]
        Список числовых значений, прочитанных из файла.
    """

    result = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                value = float(row[0])
                result.append(value)
            except ValueError:
                continue

    return result


def write_data(file_path: str, data: List[Union[int, float]]) -> None:
    """
    Функция записывает данные в файл CSV

    Parameters
    ----------
    file_path : str
        Путь к файлу CSV для записи данных.
    data : List[Union[int, float]]
        Список числовых значений для записи в файл.

    Returns
    -------
    None
    """

    with open(file_path, mode="w", encoding="utf-8", newline='') as file:
        csv_writer = csv.writer(file)
        for value in data:
            csv_writer.writerow([value])
