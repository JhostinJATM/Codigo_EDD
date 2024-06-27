
import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb
class Connection():
    def __init__(self):
        self.__db = None 

    @property
    def _db(self):
        return self.__db

    @_db.setter
    def _db(self, value):
        self.__db = value

    def connection(self, user, password, db, host="localhost"):
        self.__db = MySQLdb.connect(host=host,user=user, passwd=password, db=db,cursorclass = MySQLdb.cursors.DictCursor)
        return self
    def close(self):
        self.__db.close()