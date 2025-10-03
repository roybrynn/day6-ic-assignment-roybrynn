# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html


def my_adder(a: float, b: float, c: float) -> float:
    """
    Sums the input variables a, b, and c

    Args:
        a: numeric value
        b: numeric value
        c: numeric value

    Returns:
        out: the summation of a, b, and c
    """

    # this is the summation
    out = a + b + c

    return out


def my_thermo_stat(temp: float, desired_temp: float) -> str:
    """
    Uses the given tempterature and desired temperature to model a thermostat
    by using those values to determine if the AC needs to be turned off or on.

    Args:
        temp: the starting temperature
        desired_temp: the desired/end temperature

    Returns:
        status: the resulting action of comparing temp and desired temp
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


def have_digits(s: str) -> int:
    """
    Checks if a string contains numbers.

    Args:
        s: string value to check for numbers

    Returns:
        out: binary indicator for presence of digits
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out
