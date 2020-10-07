@fetch_student @fetch_student_by_id
Feature: Fetch students by id
  As an user of this service,
  I want to fetch student(s) by their id.

  Scenario Outline: Basic fetch student by valid id
    When the student API is queried with id
      | id            |
      | <student_ids> |
    Then the response status code is "200"

    Examples: Valid
      | student_ids |
      | 1           |

  Scenario Outline: Basic fetch student by invalid id
    When the student API is queried with id
      | id            |
      | <student_ids> |
    Then the response status code is "404"

    Examples: Invalid
      | student_ids |
      | 999         |