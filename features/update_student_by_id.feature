@update_student
Feature: Update students by id
  As an user of this service,
  I want to update student by their id.

  Scenario Outline: Basic update student by valid id
    When the update student API is queried with id
      | id            | class     |
      | <student_ids> | <classes> |
    Then the response status code is "200"

    Examples: Valid
      | student_ids | classes |
      | 891         | 9 Y     |

  Scenario Outline: Basic update student by invalid id
    When the update student API is queried with id
      | id            | class     |
      | <student_ids> | <classes> |
    Then the response status code is "404"

    Examples: Invalid
      | student_ids | classes |
      | 990         | 5 C     |
