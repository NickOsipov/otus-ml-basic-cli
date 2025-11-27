"""
Test: tests/test_model.py
Description: Тесты для модуля model.py.
"""

import pytest

from src.model import LinearModel


@pytest.mark.parametrize("weight, intercept, input_values, expected", [
    (1, 0, [0, 1, 2], [0, 1, 2]),
    (2, 3, [0, 1, 2], [3, 5, 7]),
    (0, 5, [0, 1, 2], [5, 5, 5]),
])
def test_predict(weight, intercept, input_values, expected):
    """
    Тестирует метод predict класса LinearModel.

    Parameters
    ----------
    weight : Union[int, float]
        Коэффициент наклона линии.
    intercept : Union[int, float]
        Свободный член.
    input_values : List[Union[int, float]]
        Входные значения для предсказания.
    expected : List[Union[int, float]]
        Ожидаемые выходные значения.
    """

    model = LinearModel(weight=weight, intercept=intercept)
    result = model.predict(input_values)
    assert result == expected
