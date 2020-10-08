[![codecov](https://codecov.io/gh/ketan55patil/student_enrollment_api/branch/master/graph/badge.svg)](https://codecov.io/gh/ketan55patil/student_enrollment_api/branch/master)

# Student Enrollment API

REST API for student enrollment project for a school.

_(following instructions are for Mac OS they might slightly differ for other OSs)_

## To BUILD this project
1. Install python 3.8 [link](https://formulae.brew.sh/formula/python@3.8#default)
1. Install pipenv [link](https://formulae.brew.sh/formula/pipenv#default)
1. Create virtual environment and install dependencies using [Pipfile](https://github.com/ketan55patil/student_enrollment_api/blob/master/Pipfile) and [Pipfile.lock](https://github.com/ketan55patil/student_enrollment_api/blob/master/Pipfile.lock)
    1. from projects home directory run `pipenv install --dev` (--dev will install dev packages used for testing)
1. Install and configure MySQL db (update db config in [db_utils](https://github.com/ketan55patil/student_enrollment_api/blob/master/db_utils/db_utils.py#L8) as per the local db setup)
    1. unzip and use [db_dump_20201007.sql.zip](https://github.com/ketan55patil/student_enrollment_api/blob/master/performanceTests/data/db_dump_20201007.sql.zip) to import test db and data


## To RUN this project
* Start flask
    * `pipenv run python3 student_api.py`
* go to `http://127.0.0.1:5000`

## To TEST this project
* Unit Tests:
    * run `pipenv run pytest -s test_student_api.py test_db_utils.py` from project`s home directory
* Integration Tests:
    * run `pipenv run pytest -s test_app_db_integration.py` from project`s home directory
* BDD Tests
    * run `pipenv run behave` from project`s home directory
* Performance Tests:
    * Tests are written in Jmeter
    * For execution install Jmeter
    * Use tests available in [PerformanceTest](https://github.com/ketan55patil/student_enrollment_api/tree/master/performanceTests) folder
    * Test data is available under [Data](https://github.com/ketan55patil/student_enrollment_api/tree/master/performanceTests/data)
    * Make sure correct listner (disable the `View Results Tree` listner) is selected before running the test
    * Run the tests using CLI
    * All the test fragments could be controlled using [controllerStudentAPI.jmx](https://github.com/ketan55patil/student_enrollment_api/blob/master/performanceTests/controllerStudentAPI.jmx)
      
* Code coverage captured using [codecov](https://codecov.io/gh/ketan55patil/student_enrollment_api/branch/master)
[![codecov](https://codecov.io/gh/ketan55patil/student_enrollment_api/branch/master/graph/badge.svg)](https://codecov.io/gh/ketan55patil/student_enrollment_api/branch/master)

* Github project [Link](https://github.com/ketan55patil/student_enrollment_api/projects/1)