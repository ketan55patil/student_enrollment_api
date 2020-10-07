@create_student
Feature: Create students
  As an user of this service,
  I want to create new student record.

  Scenario Outline: Basic create new student with unique id
    When the student API is queried with post data
      | class     | id    | firstName     | lastName      | nationality     |
      | <classes> | <ids> | <firstNames>  | <lastNames>  | <nationalities> |
    Then the response status code is "201"

    Examples: Valid
      | classes | ids | firstNames  | lastNames  | nationalities  |
      | 4 C     | 890 | Jack        | Wu         | China          |
      | 9 Z     | 891 | Jill        | Wong       | Bhutan         |

  Scenario Outline: Basic create new student with existing id
    When the student API is queried with post data
      | class     | id    | firstName     | lastName      | nationality     |
      | <classes> | <ids> | <firstNames>  | <lastNames>  | <nationalities> |
    Then the response status code is "400"

    Examples: Invalid
      | classes | ids | firstNames  | lastNames  | nationalities  |
      | 4 C     | 1   | Jack        | Wu         | China          |
      | 9 Z     | 2   | Jill        | Wong       | Bhutan         |

    # TODO: Create more scenarios for other invalid and missing parameters
