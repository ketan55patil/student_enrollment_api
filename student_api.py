from flask import Flask
from flask_restful import Api, Resource, reqparse
import db_utils

app = Flask(__name__)
api = Api(app)

# Request parser for creating new student record
student_post_args = reqparse.RequestParser()
student_post_args.add_argument("id", type=int,
                               help="Required field id is missing or should be int", required=True)
student_post_args.add_argument("firstName", type=str,
                               help="Required field firstName is missing", required=True)
student_post_args.add_argument("lastName", type=str,
                               help="Required field lastName is missing", required=True)
student_post_args.add_argument("class", type=str,
                               help="Required field id class missing", required=True)
student_post_args.add_argument("nationality", type=str,
                               help="Required field nationality is missing", required=True)


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
        # if not db_utils.is_unique_id(student_id):
        #     print("############# inside if")
        #     logging.error(f"id {student_id} is not unique!!!!")
        #     return "Error Id already exists!", 400

        # TODO: Validate Class and Nationality
        # If class and nationality is not valid
        #   return http 400

        # Add data to db
        cnx = db_utils.db_connect()
        if not cnx:
            ins = db_utils.db_insert_student_details(cnx, student_id, first_name, last_name,
                                                     student_class, nationality)
            db_utils.db_close_cnx(cnx)
            if ins:
                # if Successful return "Success with http 201 (created)"
                return student_details, 201

        return student_details, 400


api.add_resource(Student, "/")

if __name__ == "__main__":
    app.run(debug=True)
