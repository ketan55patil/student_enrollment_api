import mysql.connector
from mysql.connector import errorcode
import logging
import logging.config

logging.config.fileConfig('logging.conf')


def db_connect(db_host="127.0.0.1", db_user="root", db_pass="1234", db_name="student_db"):

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
                              student_class=None, nationality=None, db_table_name='student_tbl'):

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


def db_close_cnx(cnx):
    logging.debug('Closing DB connection')
    cnx.close()
