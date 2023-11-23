from main import check_arguments, check_csv, format_old_file, create_new_file
import pytest
import sys


def test_check_arguments():
    with pytest.raises(SystemExit):
        assert check_arguments()

