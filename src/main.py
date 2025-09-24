import csv
from pathlib import Path

from config import config_arg_parser
from reports import report_students_performance

DATA_FOLDER = Path("./data")


def read_students_results(filename):
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            csvreader = csv.DictReader(file)
            return list(csvreader)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return


def main():
    arg_parser = config_arg_parser()
    args = arg_parser.parse_args()
    if args.report == "students-performance":
        common_data = []
        for filename in args.files:
            file_path = DATA_FOLDER / filename
            input_data = read_students_results(file_path)
            common_data.extend(input_data)
        report_students_performance(common_data)
    else:
        print(
            "Укажите вариант отчета. Например: '--report students-performance'"
        )


if __name__ == "__main__":
    main()
