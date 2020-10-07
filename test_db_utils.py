import db_utils.db_utils as dbu


class TestDBUtils:
    # #####################################
    # db_connect
    # #####################################
    def test_db_connect_success(self):
        assert dbu.db_connect()

    def test_db_connect_invalid_username(self):
        assert not dbu.db_connect(db_user="invalid")

    def test_db_connect_invalid_db_name(self):
        assert not dbu.db_connect(db_name="invalid")

    # TODO: Uncomment this test
    # def test_db_connect_invalid_db_host(self):
    #     assert not db_utils.db_connect(db_host="invalid")

    # #####################################
    # db_insert_student_details
    # #####################################

    def test_db_insert_student_details_success(self):
        cnx = dbu.db_connect()
        is_insert = dbu.db_insert_student_details(cnx, student_id=4, first_name='Ian', last_name='Thomas',
                                                  student_class='6 B', nationality='Singapore')
        assert is_insert

    def test_db_insert_student_details_missing_params(self):
        cnx = dbu.db_connect()
        is_insert = dbu.db_insert_student_details(cnx)
        assert not is_insert

    # #####################################
    # db_fetch_students
    # #####################################

    def test_db_fetch_students_by_id(self):
        cnx = dbu.db_connect()
        expected_student_json = [{"id": 1,
                                  "first_name": "John",
                                  "lastName": "Smith",
                                  "class": "4 C",
                                  "nationality": "USA"}]

        students_json = dbu.db_fetch_students(cnx, student_id=1)
        dbu.db_close_cnx(cnx)
        assert students_json == expected_student_json

    def test_db_fetch_students_by_class(self):
        cnx = dbu.db_connect()
        expected_student_json = [{"id": 1,
                                  "first_name": "John",
                                  "lastName": "Smith",
                                  "class": "4 C",
                                  "nationality": "USA"},
                                 {"id": 2,
                                  "first_name": "Jane",
                                  "lastName": "Doe",
                                  "class": "4 C",
                                  "nationality": "Canada"}]

        students_json = dbu.db_fetch_students(cnx, student_class='4 C')
        assert students_json == expected_student_json

    def test_db_fetch_students_by_id_and_class(self):
        cnx = dbu.db_connect()
        expected_student_json = [{"id": 1,
                                  "first_name": "John",
                                  "lastName": "Smith",
                                  "class": "4 C",
                                  "nationality": "USA"}]

        students_json = dbu.db_fetch_students(cnx, student_id=1, student_class='4 C')
        dbu.db_close_cnx(cnx)
        assert students_json == expected_student_json

    def test_db_fetch_students_by_invalid_id_class_combo(self):
        cnx = dbu.db_connect()
        student_id = 1
        student_class = '5 C'

        students_text = dbu.db_fetch_students(cnx, student_id=student_id,
                                              student_class=student_class)
        dbu.db_close_cnx(cnx)
        assert not students_text

    # #####################################
    # db_update_student
    # #####################################

    def test_db_update_student_missing_id(self):
        cnx = dbu.db_connect()
        is_update = dbu.db_update_student(cnx, student_class='1 C')
        assert not is_update

    def test_db_update_student_missing_update_data(self):
        cnx = dbu.db_connect()
        is_update = dbu.db_update_student(cnx, student_id=4)
        assert not is_update

    def test_db_update_student_success(self):
        cnx = dbu.db_connect()
        is_update = dbu.db_update_student(cnx, student_id=4, student_class='1 C')
        assert is_update

    # #####################################
    # db_delete_student
    # #####################################

    def test_db_delete_student_success(self):
        cnx = dbu.db_connect()
        is_delete = dbu.db_delete_student(cnx, student_id=4)
        assert is_delete

    def test_db_delete_student_missing_id(self):
        cnx = dbu.db_connect()
        is_delete = dbu.db_delete_student(cnx)
        assert not is_delete
