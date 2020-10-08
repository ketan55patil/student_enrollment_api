import requests

base_url = "http://127.0.0.1:5000/"


class TestStudentAPI:
    # #####################################
    #  Create student record Tests
    # #####################################

    def test_post_create_student_id_201(self):
        response = requests.post(base_url, {"id": 3,
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 201

    def test_post_create_student_existing_id_409(self):
        response = requests.post(base_url, {"id": 3,
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 409

    def test_post_create_student_empty_id_400(self):
        response = requests.post(base_url, {"id": None,
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_invalid_id_400(self):
        response = requests.post(base_url, {"id": 'invalid',
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_no_id_400(self):
        response = requests.post(base_url, {"firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_no_first_name_400(self):
        response = requests.post(base_url, {"id": 3,
                                            "lastName": "Smith",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_no_last_name_400(self):
        response = requests.post(base_url, {"id": 3,
                                            "firstName": "Steve",
                                            "class": "5 D",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_no_class_400(self):
        response = requests.post(base_url, {"id": 3,
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "nationality": "USA"})
        assert response.status_code == 400

    def test_post_create_student_no_nationality_400(self):
        response = requests.post(base_url, {"id": 3,
                                            "firstName": "Steve",
                                            "lastName": "Smith",
                                            "class": "5 D"})
        assert response.status_code == 400

    # #####################################
    # Update Student Record Tests
    # #####################################

    def test_put_update_student_no_id_400(self):
        response = requests.put(base_url, {"class": "5 C"})
        assert response.status_code == 400

    def test_put_update_student_invalid_id_404(self):
        response = requests.put(base_url, {"id": 9999,
                                           "class": "5 C"})
        assert response.status_code == 404

    def test_put_update_student_only_id_400(self):
        response = requests.put(base_url, {"id": 3})
        assert response.status_code == 400

    def test_put_update_student_by_id_200(self):
        response = requests.put(base_url, {"id": 3,
                                           "class": "5 C"})
        assert response.status_code == 200

    # TODO add more cases for other combinations

    # #####################################
    # Fetch Student Record Tests
    # #####################################
    def test_get_fetch_students_by_id_200(self):
        response = requests.get(base_url + "fetchStudents", {"id": 1})
        assert response.status_code == 200

    def test_get_fetch_students_by_invalid_id_404(self):
        response = requests.get(base_url + "fetchStudents", {"id": 9999})
        assert response.status_code == 404

    def test_get_fetch_students_by_class_200(self):
        response = requests.get(base_url + "fetchStudents", {"class": "4 C"})
        assert response.status_code == 200

    def test_get_fetch_students_by_invalid_class_404(self):
        response = requests.get(base_url + "fetchStudents", {"class": "999 Z"})
        assert response.status_code == 404

    def test_get_fetch_students_by_id_and_class_200(self):
        response = requests.get(base_url + "fetchStudents", {"id": 1,
                                                             "class": "4 C"})
        assert response.status_code == 200

    def test_get_fetch_students_invalid_id_class_combo_404(self):
        response = requests.get(base_url + "fetchStudents", {"id": 1,
                                                             "class": "5 C"})
        assert response.status_code == 404

    # #####################################
    # Delete Student Record Tests
    # #####################################
    def test_delete_student_by_id_204(self):
        response = requests.delete(base_url + "3")
        assert response.status_code == 204

    def test_delete_student_by_invalid_id_404(self):
        response = requests.delete(base_url + "9999")
        assert response.status_code == 404
