@fetch_student @fetch_student_by_class
Feature: Fetch students by class
  As an user of this service,
  I want to fetch student(s) by their class.

  Scenario Outline: Basic fetch student by valid class
    When the student API is queried with class
      | class     |
      | <classes> |
    Then the response status code is "200"

    Examples: Valid
      | classes |
      | 4 C     |

  Scenario Outline: Basic fetch student by invalid class
    When the student API is queried with class
      | class     |
      | <classes> |
    Then the response status code is "400"

    Examples: Invalid
      | classes |
      | 9999 C  |
