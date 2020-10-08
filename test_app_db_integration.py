import requests
import db_utils.db_utils as dbu

base_url = "http://127.0.0.1:5000/"


class TestAppDbIntegration:
    # #####################################
    #  Create student record Tests
    # #####################################

    def test_create_student_valid_id(self):
        # input
        student_id = 3
        first_name = "Steve"
        last_name = "Smith"
        student_class = "5 D"
        nationality = "USA"

        # expected output
        expected_output = [{"id": student_id,
                            "first_name": first_name,
                            "lastName": last_name,
                            "class": student_class,
                            "nationality": nationality}]

        # Make API call
        response = requests.post(base_url, {"id": student_id,
                                            "firstName": first_name,
                                            "lastName": last_name,
                                            "class": student_class,
                                            "nationality": nationality})

        if response.status_code == 201:
            # Verify in db if student creation was successful
            # Caution: Test will be marked pass for existing record
            #          else is required to fail the test
            cnx = dbu.db_connect()
            student_details = dbu.db_fetch_students(cnx, student_id=student_id)
            dbu.db_close_cnx(cnx)
            assert student_details == expected_output
        else:
            assert False

    # #####################################
    # Update Student Record Tests
    # #####################################

    def test_update_student_valid_id(self):
        student_id = 3
        first_name = "Steve"
        last_name = "Smith"
        student_class = "5 C"
        nationality = "USA"

        expected_output = [{"id": student_id,
                            "first_name": first_name,
                            "lastName": last_name,
                            "class": student_class,
                            "nationality": nationality}]

        response = requests.put(base_url, {"id": student_id,
                                           "class": student_class})
        if response.status_code == 200:
            cnx = dbu.db_connect()
            student_details = dbu.db_fetch_students(cnx, student_id=student_id)
            dbu.db_close_cnx(cnx)
            assert student_details == expected_output
        else:
            assert False

    # #####################################
    # Fetch Student Record Tests
    # #####################################

    def test_fetch_students_valid_id_class(self):
        student_id = 3
        first_name = "Steve"
        last_name = "Smith"
        student_class = "5 C"
        nationality = "USA"

        expected_output = [{"id": student_id,
                            "first_name": first_name,
                            "lastName": last_name,
                            "class": student_class,
                            "nationality": nationality}]

        response = requests.get(base_url + "fetchStudents", {"id": student_id,
                                                             "class": "5 C"})
        if response.status_code == 200:
            cnx = dbu.db_connect()
            student_json = dbu.db_fetch_students(cnx, student_id=student_id,
                                                 student_class=student_class)
            dbu.db_close_cnx(cnx)
            assert student_json == expected_output
        else:
            assert False

    # #####################################
    # Delete Student Record Tests
    # #####################################

    def test_delete_student_valid_id(self):
        student_id = 3
        response = requests.delete(base_url + f"{student_id}")
        if response.status_code == 204:
            cnx = dbu.db_connect()
            student_details = dbu.db_fetch_students(cnx, student_id=student_id)
            dbu.db_close_cnx(cnx)
            assert not student_details
        else:
            assert False

