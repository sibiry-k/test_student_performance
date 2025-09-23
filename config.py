import argparse

def config_arg_parser():
    parser = argparse.ArgumentParser(
        prog="poetry run python main.py",
        description=("Эта программа выполняет анализ успеваемости "
                     "студентов на основе данных из CSV-файла."),
    )
    parser.add_argument(
        '--files',
        nargs='+',
        help=("Cписок файлов для обработки "
              "(Например: students1.csv, students2.csv)"),
    )
    parser.add_argument(
        '--report',
        help='результат обработки'
    )
    return parser