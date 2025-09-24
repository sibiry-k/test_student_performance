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

    if args.files is None:
        print("Проверьте указание атрибутов. Например: '--files students1.csv")
        return

    if args.report == "students-performance":
        common_data = []
        for filename in args.files:
            file_path = DATA_FOLDER / filename
            input_data = read_students_results(file_path)
            if input_data:
                common_data.extend(input_data)
            else:
                return
        report_students_performance(common_data)
    else:
        print("Проверьте аргументы. Например: '--report students-performance'")
        return


if __name__ == "__main__":
    main()
