import db_utils


class TestDBUtils:
    # #####################################
    # db_connect
    # #####################################
    def test_db_connect_success(self):
        assert db_utils.db_connect()

    def test_db_connect_invalid_username(self):
        assert not db_utils.db_connect(db_user="invalid")

    def test_db_connect_invalid_db_name(self):
        assert not db_utils.db_connect(db_name="invalid")

    # TODO: Uncomment this test
    # def test_db_connect_invalid_db_host(self):
    #     assert not db_utils.db_connect(db_host="invalid")

    # #####################################
    # db_insert_student_details
    # #####################################

    def test_db_insert_student_details_success(self):
        cnx = db_utils.db_connect()
        is_insert = db_utils.db_insert_student_details(cnx, student_id=4, first_name='Ian', last_name='Thomas',
                                                       student_class='6 B', nationality='Singapore')
        assert is_insert

    def test_db_insert_student_details_missing_params(self):
        cnx = db_utils.db_connect()
        is_insert = db_utils.db_insert_student_details(cnx)
        assert not is_insert
