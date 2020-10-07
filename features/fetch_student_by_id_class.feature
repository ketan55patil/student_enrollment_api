@fetch_student @fetch_student_by_id_class
Feature: Fetch students by id and class
  As an user of this service,
  I want to fetch student(s) by their id and class.

  Scenario Outline: Basic fetch student by valid id and class
    When the student API is queried with
      | id            | class     |
      | <student_ids> | <classes> |
    Then the response status code is "200"

    Examples: Valid
      | student_ids | classes |
      | 1           | 4 C     |
      | 2           | 4 C     |
      | 9           | 9 Z     |
  Scenario Outline: Basic fetch student by invalid id and class
    When the student API is queried with
      | id            | class     |
      | <student_ids> | <classes> |
    Then the response status code is "400"

    Examples: Invalid
      | student_ids | classes |
      | 999         | 4 C     |
      | 998         | 4 C     |
      | 997         | 9 Z     |
