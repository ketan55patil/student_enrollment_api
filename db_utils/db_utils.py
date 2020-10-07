import mysql.connector
from mysql.connector import errorcode
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# TODO: Move this to a config file
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASS = "1234"
DB_NAME = "student_db"
DB_TABLE_NAME = 'student_tbl'


def db_connect(db_host=DB_HOST, db_user=DB_USER, db_pass=DB_PASS, db_name=DB_NAME):

    try:
        cnx = mysql.connector.connect(user=db_user, password=db_pass,
                                      host=db_host,
                                      database=db_name)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Incorrect username or password")

            return False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("Database does not exist")
            return False
        else:
            logging.error(err)
            return False


def db_insert_student_details(cnx, student_id=None, first_name=None, last_name=None,
                              student_class=None, nationality=None, db_table_name=DB_TABLE_NAME):

    sql_insert = f"INSERT INTO {db_table_name} " \
                 f"(id, firstName, lastName, class, nationality) \
                     VALUES (%s, %s, %s, %s, %s)"

    cursor = cnx.cursor()

    row_list = (student_id, first_name, last_name, student_class, nationality)

    logging.debug(f'Attempting to insert {row_list}...')
    try:
        cursor.execute(sql_insert, row_list)
    except mysql.connector.Error as err:
        logging.error(err)
        return False

    logging.debug('Committing insert...')
    cnx.commit()

    logging.debug('Closing cursor')
    cursor.close()
    return True


def db_update_student(cnx, student_id=None, first_name=None, last_name=None,
                      student_class=None, nationality=None, db_table_name=DB_TABLE_NAME):
    set_string_list = []
    if first_name is not None:
        set_string_list.append(f"firstName = '{first_name}'")

    if last_name is not None:
        set_string_list.append(f"lastName = '{last_name}'")

    if student_class is not None:
        set_string_list.append(f"class = '{student_class}'")

    if nationality is not None:
        set_string_list.append(f"nationality = '{nationality}'")

    logging.debug(f"set_string_dict is: {set_string_list}")
    if not set_string_list:
        logging.debug("Nothing to update")
        return False

    set_string = ', '.join(set_string_list)

    sql_update = f"UPDATE {db_table_name} " \
                 f"SET {set_string} " \
                 f"WHERE id = {student_id}"

    logging.debug(f'Sql update query is:  {sql_update}...')

    cursor = cnx.cursor()

    logging.debug(f'Attempting to update {set_string}...')

    try:
        cursor.execute(sql_update)
    except mysql.connector.Error as err:
        logging.error(err)
        return False

    logging.debug('Committing update...')
    cnx.commit()

    logging.debug('Closing cursor')
    cursor.close()
    return True


def db_fetch_students(cnx, student_id=None, student_class=None, db_table_name=DB_TABLE_NAME):
    cursor = cnx.cursor()

    logging.debug(f"student_id is {student_id} and "
                  f"student_class is {student_class}")

    # TODO: Limit the number of records being fetched form the db at a time
    where_list = []
    if student_class is not None:
        where_list.append(f"class='{student_class}'")
    if student_id is not None:
        where_list.append(f"id={student_id}")

    if not where_list:
        logging.error("student id or class is required")
        return False

    where_string = ' and '.join(where_list)

    sql_select = f"SELECT id, firstName, lastName, class, nationality " \
                 f"FROM {db_table_name} " \
                 f"WHERE {where_string}"

    logging.debug(f"query = {sql_select}")
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    students_list = []

    logging.debug(f"cursor.rowcount is {cursor.rowcount}")

    if student_id is not None and student_id is not None and len(rows) == 0:
        logging.error(f"No records found for id {student_id} and class {student_class}!")
        return False

    if student_id is not None and len(rows) == 0:
        logging.error(f"No records found for id {student_id}!")
        return False
    if student_class is not None and len(rows) == 0:
        logging.error(f"No records found for class {student_class}!")
        return False

    for col in rows:
        student_dict = {"id": col[0],
                        "first_name": col[1],
                        "lastName": col[2],
                        "class": col[3],
                        "nationality": col[4]}

        students_list.append(student_dict)

    logging.debug(f"Students list is: {students_list}")
    logging.debug('Closing cursor')
    cursor.close()
    return students_list


def db_delete_student(cnx, student_id=None, db_table_name=DB_TABLE_NAME):
    sql_delete = f"DELETE FROM {db_table_name} " \
                 f"WHERE id = {student_id}"

    logging.debug(f'Sql delete query is:  {sql_delete}...')

    cursor = cnx.cursor()

    logging.debug(f'Attempting to delete record for student_id {student_id}...')

    try:
        cursor.execute(sql_delete)
    except mysql.connector.Error as err:
        logging.error(err)
        return False

    logging.debug('Committing update...')
    cnx.commit()

    if cursor.rowcount == 1:
        logging.debug("Deleted exactly 1 record")
        logging.debug('Closing cursor')
        cursor.close()
        return True

    if cursor.rowcount < 1:
        logging.error("No records found to delete!")

    if cursor.rowcount > 1:
        logging.error("Deleted more than 1 records!")

    logging.debug('Closing cursor')
    cursor.close()
    return False


def db_close_cnx(cnx):
    logging.debug('Closing DB connection')
    cnx.close()
