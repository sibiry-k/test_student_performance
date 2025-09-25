from unittest.mock import MagicMock, mock_open, patch

from config import config_arg_parser
from main import main, read_students_results
from reports import report_students_performance


class TestReadCSV:
    """Тесты для проверки открытия csv-файла."""

    def test_read_students_results_valid(self, csv_valid):
        """Проверяем корректное открытие файла."""
        mock_file = mock_open(read_data=csv_valid)
        with patch("builtins.open", mock_file):
            csv_data = read_students_results("test_students.csv")
            assert isinstance(csv_data, list)
            assert len(csv_data) == 3
            assert csv_data[0]["student_name"] == "Семенова Елена"
            assert csv_data[0]["grade"] == "5"
            assert csv_data[2]["student_name"] == "Власова Алина"
            assert csv_data[2]["grade"] == "5"

    def test_returns_none_on_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = read_students_results("file_not_found.csv")
        assert result is None


class TestReportStudentsPerformance:
    """Тесты для проверки составления отчета."""

    def test_calc_avg_for_student(self, csv_for_avg_calc_student):
        with patch(
            "builtins.open", mock_open(read_data=csv_for_avg_calc_student)
        ):
            csv_data = read_students_results("test_students.csv")
        with patch("builtins.print") as mock_print:
            report_students_performance(csv_data)
        output = mock_print.call_args[0][0]
        assert "Семенова Елена" in output
        assert "4.0" in output
        assert output.count("Семенова Елена") == 1

    def test_calc_avg_for_some_students(self, csv_for_avg_calc_some_students):
        with patch(
            "builtins.open",
            mock_open(read_data=csv_for_avg_calc_some_students),
        ):
            csv_data = read_students_results("test_students.csv")
        with patch("builtins.print") as mock_print:
            report_students_performance(csv_data)
        output = mock_print.call_args[0][0]
        assert output.count("Семенова Елена") == 1
        assert "4.5" in output
        assert output.count("Титов Владислав") == 1
        assert "4.0" in output
        assert output.count("Власова Алина") == 1
        assert "3.5" in output

    def test_rate_students(self, csv_for_rate_students):
        with patch(
            "builtins.open", mock_open(read_data=csv_for_rate_students)
        ):
            csv_data = read_students_results("test_students.csv")
        with patch("builtins.print") as mock_print:
            report_students_performance(csv_data)
        output = mock_print.call_args[0][0]

        top = output.find("Семенова Елена")
        middle = output.find("Титов Владислав")
        lower = output.find("Власова Алина")

        assert top < middle < lower


class TestConfigModule:
    """Тесты для проверки создания атрибутов командной строки."""

    def test_config_arg_parser(self):
        parser = config_arg_parser()
        assert parser is not None
        assert parser.prog == "poetry run python main.py"

    def test_config_arg_parser_args_files(self):
        parser = config_arg_parser()
        args = parser.parse_args(["--files", "test1.csv", "test2.csv"])
        assert args.files == ["test1.csv", "test2.csv"]

    def test_config_arg_parser_args_report(self):
        parser = config_arg_parser()
        args = parser.parse_args(["--report", "test-student"])
        assert args.report == "test-student"

    def test_config_arg_parser_no_args(self):
        parser = config_arg_parser()
        args = parser.parse_args([])
        assert args.report is None
        assert args.files is None


class TestMainModule:
    """Тесты для проверки работы главного модуля."""

    @patch("main.config_arg_parser")
    def test_main_no_args_files(self, mock_parser):
        mock_args = MagicMock()
        mock_args.files = None
        mock_parser.return_value.parse_args.return_value = mock_args

        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_called_once_with(
            "Проверьте аргументы. Например: '--files students1.csv"
        )

    @patch("main.config_arg_parser")
    def test_main_no_csv_file(self, mock_parser):
        mock_args = MagicMock()
        mock_args.files = ["test1.txt", "test2.csv"]
        mock_parser.return_value.parse_args.return_value = mock_args

        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_called_once_with(
            "Скрипт обрабатывает только CSV-файлы."
        )

    @patch("main.config_arg_parser")
    def test_main_wrong_report(self, mock_parser):
        mock_args = MagicMock()
        mock_args.files = ["test.csv"]
        mock_args.report = ["wrong-report"]
        mock_parser.return_value.parse_args.return_value = mock_args

        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_called_once_with(
            "Проверьте аргументы. Например: '--report students-performance'"
        )

    @patch("main.config_arg_parser")
    @patch("main.read_students_results")
    @patch("main.report_students_performance")
    def test_main_right_work(
        self, mock_report, mock_read, mock_parser, csv_valid
    ):
        mock_args = MagicMock()
        mock_args.files = ["test1.csv"]
        mock_args.report = "student-performance"
        mock_parser.return_value.parse_args.return_value = mock_args

        with patch("builtins.open", mock_open(read_data=csv_valid)):
            csv_data = read_students_results("test_students.csv")
        mock_read.return_value = csv_data

        main()

        mock_read.assert_called_once()
        mock_report.assert_called_once_with(csv_data)
