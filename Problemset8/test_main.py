# from main import Seasons
# from datetime import date
# import pytest
#
#
# def test_check_date():
#     seasons = Seasons.get_input()
#     # assert seasons.date_of_birth == date(2022, 9, 4)
#     # assert str(seasons) == "Five hundred twenty-five thousand, six hundred minutes"
#     with pytest.raises(SystemExit) as e:
#         Seasons.get_input()
#     assert e.type == SystemExit


from main import get_date, get_minutes, format_minutes


def test_format_output():
    assert format_minutes(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert format_minutes(1050200) == "One million, fifty thousand, two hundred minutes"




