import pytest
import runpy

from pytest_bdd import scenarios, given, when, then, parsers, scenario


@scenario('/Users/shmeka/PycharmProjects/CSC256/retirement.feature', 'Check the retirement')
def test_retirement():
    pass


@given("the program is running")
def program_running():
    runpy.run_path(path_name='hello.py')

# @when('you input a birth year of 1937, or earlier, and birth month')
