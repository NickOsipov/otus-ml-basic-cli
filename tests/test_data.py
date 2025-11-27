"""
Test: tests/test_data.py
Description: Тесты для модуля data.py.
"""

import os

from src.data import read_data

def test_read_data():
    """
    Тестирует функцию read_data для корректного чтения данных из CSV файла.
    """
    test_file_path = os.path.join("data", "test.csv")
    
    result = read_data(test_file_path)
    
    expected = [1.0, 2.0, 3.0, 4.0, 5.0]
    
    assert result == expected