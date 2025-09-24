from tabulate import tabulate


def report_students_performance(data):
    table = {}

    # Формируем словарь {Студент: список оценок}
    for row in data:
        student_name = row["student_name"]
        grade = int(row["grade"])
        table.setdefault(student_name, []).append(grade)

    # Формируем итоговый словарь {Студент: средняя оценка}
    result_table = {
        student: sum(grade) / len(grade) for student, grade in table.items()
    }

    # Сортируем итоговый словарь по средней оценке
    rows = sorted(
        ((student, f"{avg:.1f}") for student, avg in result_table.items()),
        key=lambda x: float(x[1]),
        reverse=True,
    )

    # Добавляем счётчик
    result_rows = [
        (i, student, avg) for i, (student, avg) in enumerate(rows, start=1)
    ]

    print(
        tabulate(
            result_rows,
            headers=["", "student_name", "grade"],
            tablefmt="pretty",
        )
    )
