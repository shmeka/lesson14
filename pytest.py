import pytest
from _pytest.pathlib import parse_num
from retirement import *
from functools import partial
from pytest_bdd import scenarios, given, when, then, parsers, scenario
import retirement



EXTRA_TYPES = {
    'Number': int,
    'String': str,
}


# check year 1937 month 1
@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 1937 month 1')
def test_retirement():
    pass


@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    return retirement._validate_birth_year(year)


@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return retirement._validate_birth_month(month)


@then(parsers.cfparse('your retirement age "{rAge:Number}" years and "{rMonths:Number}" month(s) will be shown', extra_types=EXTRA_TYPES))
def return_retirement_date_age(rAge, rMonths):
    input_year = calculate_retirement_age(1937)
    return input_year == (rAge, rMonths)



@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 1990 month 12')
def test_retirement():
    pass


@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    return retirement._validate_birth_year(year)


@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return retirement._validate_birth_month(month)


@then(parsers.cfparse('your retirement age "{rAge:Number}" years and "{rMonths:Number}" month(s) will be shown', extra_types=EXTRA_TYPES))
def return_retirement_date_age(rAge, rMonths):
    input_year = calculate_retirement_age(1990)
    return input_year == (rAge, rMonths)



# check year 1888 month 12
@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 1888 month 12')
def test_retirement():
    pass

@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    assert retirement._validate_birth_year(year)
    raise ValueError('Birth year "year" must be no earlier than 1900')

@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return retirement._validate_birth_month(month)

@then(parsers.cfparse('"{error:String}" will be shown', extra_types=EXTRA_TYPES))
def return_error():
    return ValueError('Birth year "year" must be no earlier than 1900')


# check year 3333 month 12
@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 3333 month 12')
def test_retirement():
    pass

@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    return retirement._validate_birth_year(year)
@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return retirement._validate_birth_month(month)

@then(parsers.cfparse('"{error:String}" will be shown', extra_types=EXTRA_TYPES))
def return_error():
    return ValueError('Birth year "year" must be no later than 1900')

# check year 1937 month 99
@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 1937 month 33')
def test_retirement():
    pass


@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    return retirement._validate_birth_year(year)


@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return 'Birth month "{month}" must be between 1 and 12'


@then(parsers.cfparse('"{error:String}" will be shown', extra_types=EXTRA_TYPES))
def return_error():
    return ValueError('Birth month "month" must be between 1 and 12')

# check year 1937 month 99
@scenario('/Users/shmeka/PycharmProjects/lesson14/retirement.feature', 'Check the retirement year 1937 month -1')
def test_retirement():
    pass


@given(parsers.cfparse('the birth year is "{year:Number}"', extra_types=EXTRA_TYPES))
def birth_year(year):
    return retirement._validate_birth_year(year)


@when(parsers.cfparse('you input a birth month of "{month:Number}"', extra_types=EXTRA_TYPES))
def birth_month(month):
    return 'Birth month "{month}" must be between 1 and 12'


@then(parsers.cfparse('"{error:String}" will be shown', extra_types=EXTRA_TYPES))
def return_error():
    return ValueError('Birth month "month" must be between 1 and 12')

