@delete_student_by_id
Feature: Delete students by id
  As an user of this service,
  I want to delete student(s) by their id.

  Scenario Outline: Basic delete student by valid id
    When the delete student API is queried with id
      | id            |
      | <student_ids> |
    Then the response status code is "204"

    Examples: Valid
      | student_ids |
      | 890         |
  Scenario Outline: Basic delete student by invalid id
    When the delete student API is queried with id
      | id            |
      | <student_ids> |
    Then the response status code is "404"

    Examples: Invalid
      | student_ids |
      | 999         |
