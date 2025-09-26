# test_student_performance
Тестовое задание на позицию Junior Backend Python Developer в WorkMate

## Стек
Менеджер пакетов - <b>poetry</b><br>
Линтер, форматер - <b>ruff</b><br>
Также использован <b>pre-commit</b>

## Установка проекта
1. Клонировать проект локально:
   ```git clone git@github.com:sibiry-k/test_student_performance.git```
3. Установить Poetry:
   ```pip install poetry```
4. Установить зависимости проекта
   ```poetry install```


## Запуск скрипта
```poetry run python src/main.py --files students1.csv students2.csv --report student-performance```
### С одним файлом данных:
<img src="img/run_1_files.jpg" alt="Запуск с одним файлом" width="400" height="300">

### С двумя файлами данных:
<img src="img/run_2_fiels.jpg" alt="Запуск с двумя файлами" width="500" height="400">

## Запуск тестов
```poetry run pytest -v```
![Результат pytest](img/run_pytest.jpg)

## Запуск тестов с подсчетом покрытия
```poetry run pytest --cov=src tests/```
![Результат pytest coverage](img/run_pytest_with_coverage.jpg)

## Добавление новых отчетов:
В модуль ```reports.py``` добавить функцию формирования нового отчета ```def new_report```.<br>
В модуль ```main.py``` импортировать новую функцию подсчета и добавить ее в функцию ```main()``` в блок ```try``` после вызова функции ```report_students_performance```, передав в качестве аргумента ```(common_data)```.<br>
Пример: ```new_report(common_data)```
