"""
This module contains step definitions for fetch_student_by_id.feature.
It uses the requests package:
http://docs.python-requests.org/
"""
import requests
from behave import *

# "Constants"
STUDENT_API = 'http://127.0.0.1:5000/'


@when('the delete student API is queried with id')
def step_impl(context):
    first_row = context.table[0]
    context.response = requests.delete(f"{STUDENT_API}{first_row['id']}")


@then('the response status code is "{code:d}"')
def step_impl(context, code):
    assert context.response.status_code == code
