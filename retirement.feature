Feature: Check Retirement Age

Scenario: Check the retirement year 1937 month 1
	Given the birth year is "1937"
	When you input a birth month of "1"
	Then your retirement age "65" years and "0" month(s) will be shown

	Scenario Outline: Check the retirement year 1990 month 12
		Given the birth year is "1990"
		When you input a birth month of "12"
		Then your retirement age "67" years and "0" month(s) will be shown
		Examples:
		  | year  | month              | age years| age months  |
		  | 1937  | 12				   | 65 	  | 0   		|
		  | 1940  | 1				   | 65 	  | 6   		|
		  | 1954  | 12				   | 66 	  | 0   		|
		  | 1959  | 12				   | 66 	  | 10   		|
		  | 1990  | 10				   | 67 	  | 0   		|

Scenario: Check the retirement year 1888 month 12
	Given the birth year is "1888"
	When you input a birth month of "12"
	Then "Birth year must be no earlier than 1900" will be shown

Scenario: Check the retirement year 3333 month 12
	Given the birth year is "3333"
	When you input a birth month of "12"
	Then "Birth year must be no earlier than 1900" will be shown

Scenario: Check the retirement year 1937 month 33
	Given the birth year is "1937"
	When you input a birth month of "33"
	Then "Birth year must be no earlier than 1900" will be shown

Scenario: Check the retirement year 1937 month -1
	Given the birth year is "1937"
	When you input a birth month of "-1"
	Then "Birth year must be no earlier than 1900" will be shown