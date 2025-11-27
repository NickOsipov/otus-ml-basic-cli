"""
Module: model.py
Description: Модуль, содержащий простую модель линейной функции.
"""

from typing import Union, List


class LinearModel:
    """
    Простая линейная модель вида y = weight * x + intercept.

    Attributes
    ----------
    weight : Union[int, float]
        Коэффициент наклона линии.
    intercept : Union[int, float]
        Свободный член (пересечение с осью Y).
    
    Methods
    -------
    predict(values: List[Union[int, float]]) -> List[Union[int, float]]
        Предсказывает выходные значения для заданного списка входных значений.    
    """

    def __init__(self, weight: Union[int, float] = 1, intercept: Union[int, float] = 0):
        """
        Инициализирует линейную модель с заданными параметрами.

        Parameters
        ----------
        weight : Union[int, float], optional
            Коэффициент наклона линии (по умолчанию 1).
        intercept : Union[int, float], optional
            Свободный член (по умолчанию 0).
        """
        self.weight = weight
        self.intercept = intercept

    def __calc_result(self, value: Union[int, float]) -> Union[int, float]:
        """
        Вычисляет результат линейной функции для одного входного значения.

        Parameters
        ----------
        value : Union[int, float]
            Входное значение для вычисления.

        Returns
        -------
        Union[int, float]
            Результат вычисления линейной функции для данного входного значения.
        """
        return self.weight * value + self.intercept

    def predict(self, values: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        Предсказывает выходные значения для заданного списка входных значений.

        Parameters
        ----------
        values : List[Union[int, float]]
            Список входных значений для предсказания.

        Returns
        -------
        List[Union[int, float]]
            Список предсказанных выходных значений для каждого входного значения.
        """
        return [self.__calc_result(value) for value in values]
