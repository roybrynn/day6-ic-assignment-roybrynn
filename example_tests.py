# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest
from example_functions import my_adder
from example_functions import my_thermo_stat
from example_functions import have_digits


def test_pos_adder():
    assert my_adder(1, 2, 3) == 6


def test_neg_adder():
    assert my_adder(-1, -2, -3) == -6


@pytest.mark.parametrize(
    "a,b,c,expected", [(1, 2, 3, 6), (-1, -2, -3, -6), (0, 0, 0, 0)]
)
def test_adder(a, b, c, expected):
    output = my_adder(a, b, c)
    assert output == expected


def test_thermo_stat_heat():
    assert my_thermo_stat(50, 70) == "Heat"


def test_thermo_stat_ac():
    assert my_thermo_stat(70, 50) == "AC"


def test_thermo_stat_off():
    assert my_thermo_stat(65, 70) == "off"


def test_digits_with_digits():
    assert have_digits("Hi I have a 5 value") == 1


def test_digits_with_strings():
    assert have_digits("Hi I don't have a five value") == 0
