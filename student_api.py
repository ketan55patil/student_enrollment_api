from flask import Flask
from flask_restful import Api, Resource, reqparse
import db_utils.db_utils as dbu

# Create new flask app and api
app = Flask(__name__)
api = Api(app)

# Request parser for creating new student record
student_post_args = reqparse.RequestParser()
student_post_args.add_argument("id", type=int,
                               help="Required field id is missing or should be an int", required=True)
student_post_args.add_argument("firstName", type=str,
                               help="Required field firstName is missing", required=True)
student_post_args.add_argument("lastName", type=str,
                               help="Required field lastName is missing", required=True)
student_post_args.add_argument("class", type=str,
                               help="Required field id class missing", required=True)
student_post_args.add_argument("nationality", type=str,
                               help="Required field nationality is missing", required=True)

# Request parser for update Students
student_put_args = reqparse.RequestParser()
student_put_args.add_argument("id", type=int,
                              help="Required field id is missing or should be an int", required=True)
student_put_args.add_argument("firstName", type=str,
                              help="firstName should be a string")
student_put_args.add_argument("lastName", type=str,
                              help="lastName should be a string")
student_put_args.add_argument("class", type=str,
                              help="class should be a string")
student_put_args.add_argument("nationality", type=str,
                              help="nationality should be a string")

# Request parser for delete
delete_student_args = reqparse.RequestParser()
delete_student_args.add_argument("id", type=int,
                                 help="Required field id is missing or should be an int", required=True)

# Request parser for fetchStudents
fetch_students_args = reqparse.RequestParser()
fetch_students_args.add_argument("id", type=int,
                                 help="id should be an int")
fetch_students_args.add_argument("class", type=str,
                                 help="class should be a string")


class Student(Resource):

    # New student creation
    def post(self):
        student_details = student_post_args.parse_args()
        student_id = student_details["id"]
        first_name = student_details["firstName"]
        last_name = student_details["lastName"]
        student_class = student_details["class"]
        nationality = student_details["nationality"]

        # Check if id is unique
        # if not is_unique_id(student_id):
        #     logging.error(f"id {student_id} is not unique!!!!")
        #     return "Error Id already exists!", 400

        # TODO: Validate Class and Nationality
        # If class and nationality is not valid
        #   return http 400

        # Add data to db
        cnx = dbu.db_connect()
        if cnx:
            ins = dbu.db_insert_student_details(cnx, student_id, first_name, last_name,
                                                student_class, nationality)
            dbu.db_close_cnx(cnx)
            if ins:
                # if Successful return "Success with http 201 (created)"
                return student_details, 201
        return student_details, 400

    def put(self):
        # Use this for update student record
        # update if id is unique and other args are valid
        # at least 1 arg is required
        student_details = student_put_args.parse_args()
        student_id = student_details["id"]
        first_name = student_details["firstName"]
        last_name = student_details["lastName"]
        student_class = student_details["class"]
        nationality = student_details["nationality"]

        cnx = dbu.db_connect()

        is_valid_id = dbu.db_fetch_students(cnx, student_id=student_id)
        upd = None

        if is_valid_id:
            upd = dbu.db_update_student(cnx, student_id=student_id, first_name=first_name,
                                        last_name=last_name, student_class=student_class,
                                        nationality=nationality)
        if upd:
            return f"Successfully updated record for student with id {student_id}", 200
        else:
            return f"Not able to update student with id {student_id}", 400


class FetchStudents(Resource):

    def get(self):
        # id or class is required
        fetch_students = fetch_students_args.parse_args()

        student_id = fetch_students["id"]
        student_class = fetch_students["class"]

        # if student_id:
        #     cnx = dbu.db_connect()
        #     student_json = dbu.db_fetch_students(cnx, student_id=student_id)
        #     # print(f"student_json is {student_json}")
        # elif student_class:
        #     # TODO: update the query to return records by class
        #     cnx = dbu.db_connect()
        #     student_json = dbu.db_fetch_students(cnx, student_class=student_class)
        #     # print(f"student_json is {student_json}")
        # # else:
        # #     return "valid id or class is required", 400
        cnx = dbu.db_connect()
        student_json = dbu.db_fetch_students(cnx, student_id=student_id, student_class=student_class)

        # TODO: update to return the correct response
        if not student_json:
            return "valid id and/or class is required", 400
        else:
            return student_json, 200


class DeleteStudent(Resource):
    def delete(self, student_id):
        # Use this for delete student record
        # Delete if id is unique
        # if Successful return "Success with appropriate http response code"
        # student_details = delete_student_args.parse_args()
        # student_id = student_details["id"]
        cnx = dbu.db_connect()
        is_delete = dbu.db_delete_student(cnx, student_id=student_id)
        if is_delete:
            return f"Successfully deleted record for student with id {student_id}", 200
        else:
            return f"Not able to delete student with id {student_id}", 400


api.add_resource(DeleteStudent, "/<int:student_id>")
api.add_resource(Student, "/")
api.add_resource(FetchStudents, "/fetchStudents")

if __name__ == "__main__":
    # TODO: Change this false for production
    app.run(debug=True)
