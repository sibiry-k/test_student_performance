from unittest.mock import mock_open, patch

from main import read_students_results


def test_main():
    assert 1


def test_read_students_results_valid(csv_valid):
    mock_file = mock_open(read_data=csv_valid)
    with patch("builtins.open", mock_file):
        data = read_students_results("test_students.csv")
        assert isinstance(data, list)
        for row in data:
            assert "student_name" in row, "Отсутствует столбец 'student_name'"
            assert "grade" in row, "Отсутствует столбец 'grade'"
