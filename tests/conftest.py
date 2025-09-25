import pytest


@pytest.fixture
def csv_valid():
    csv_data = """student_name,subject,teacher_name,date,grade
Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
Титов Владислав,География,Орлов Сергей,2023-10-12,4
Власова Алина,Биология,Ткаченко Наталья,2023-10-15,5"""
    return csv_data


@pytest.fixture
def csv_for_avg_calc_student():
    csv_data = """student_name,subject,teacher_name,date,grade
Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
Семенова Елена,География,Орлов Сергей,2023-10-12,3
Семенова Елена,Биология,Ткаченко Наталья,2023-10-15,4"""
    return csv_data


@pytest.fixture
def csv_for_avg_calc_some_students():
    csv_data = """student_name,subject,teacher_name,date,grade
Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
Семенова Елена,География,Орлов Сергей,2023-10-12,4
Титов Владислав,География,Орлов Сергей,2023-10-12,4
Власова Алина,Биология,Ткаченко Наталья,2023-10-15,5
Власова Алина,География,Ткаченко Наталья,2023-10-15,2"""
    return csv_data


@pytest.fixture
def csv_for_rate_students():
    csv_data = """student_name,subject,teacher_name,date,grade
Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5
Титов Владислав,География,Орлов Сергей,2023-10-12,4
Власова Алина,География,Ткаченко Наталья,2023-10-15,3"""
    return csv_data
