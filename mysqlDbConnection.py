import mysql.connector
from mysql.connector import Error


def getCursor(mysqlHost, mysqlUser, mysqlPw, mysqlDb):
    try:
        connection = mysql.connector.connect(
            host=mysqlHost, user=mysqlUser, password=mysqlPw, database=mysqlDb
        )
        dbCursor = connection.cursor(buffered=True)

        return connection, dbCursor
    except Error as e:
        return None, None
