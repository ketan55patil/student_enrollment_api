"""
This module contains step definitions for create_student.feature.
It uses the requests package:
http://docs.python-requests.org/
"""
import requests
from behave import *

# "Constants"
STUDENT_API = 'http://127.0.0.1:5000/'


@when('the student API is queried with post data')
def step_impl(context):
    first_row = context.table[0]
    params = {'id': first_row['id'],
              'class': first_row['class'],
              'firstName': first_row['firstName'],
              'lastName': first_row['lastName'],
              'nationality': first_row['nationality']
              }
    context.response = requests.post(STUDENT_API, params=params)


@then('the response status code is "{code:d}"')
def step_impl(context, code):
    assert context.response.status_code == code
