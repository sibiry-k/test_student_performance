import pytest


@pytest.fixture
def csv_valid():
    csv_data = """student_name,subject,teacher_name,date,grade
       Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
       Титов Владислав,География,Орлов Сергей,2023-10-12,4
       Власова Алина,Биология,Ткаченко Наталья,2023-10-15,5"""
    return csv_data


@pytest.fixture
def csv_not_valid_column():
    csv_data = """name,subject,teacher_name,date,grade
       Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
       Титов Владислав,География,Орлов Сергей,2023-10-12,4
       Власова Алина,Биология,Ткаченко Наталья,2023-10-15,5"""
    return csv_data
