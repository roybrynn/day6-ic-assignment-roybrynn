import pytest


def my_adder(a, b, c):
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """

    # this is the summation
    out = a + b + c

    return out


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


def my_thermo_stat(temp, desired_temp):
    """
    Changes the status of the thermostat based on
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


def test_thermo_stat_heat():
    assert my_thermo_stat(50, 70) == "Heat"


def test_thermo_stat_ac():
    assert my_thermo_stat(70, 50) == "AC"


def test_thermo_stat_off():
    assert my_thermo_stat(65, 70) == "off"


def have_digits(s):
    """
    Checks if a string has digits in it
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out


def test_digits_with_digits():
    assert have_digits("Hi I have a 5 value") == 1


def test_digits_with_strings():
    assert have_digits("Hi I don't have a five value") == 0
