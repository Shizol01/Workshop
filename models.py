from connection import execute_sql
import psycopg2
from datetime import datetime

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = None

    def save(self):
        if self.id is None:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s) returning id"
            ret_val = execute_sql(sql, 'workshop', self.username, self.password)[0]
            if ret_val:
                self.id = ret_val[0]
        else:
            sql = "UPDATE users SET password = %s WHERE id = %s"
            ret_val = execute_sql(sql,'workshop', self.password, self.id)
            return True

    @classmethod
    def load_user_by_username(cls, username):
        sql = "SELECT * FROM users WHERE username = %s"
        ret_val = execute_sql(sql, 'workshop', username)
        if ret_val:
            u= cls(ret_val[0][1], ret_val[0][2])
            u.id = ret_val[0][0]
            return u.username, u.password, u.id

    @classmethod
    def load_user_by_id(cls, id):
        sql = "SELECT * FROM users WHERE id = %s"
        try:
            ret_val = execute_sql(sql, 'workshop', id)[0]
        except IndexError:
            return None
        u = cls(ret_val[1], ret_val[2])
        u.id = ret_val[0]
        return u


    @classmethod
    def load_all_users(cls):

        sql = "SELECT * FROM users"
        ret_val = execute_sql(sql, 'workshop')
        users = []
        for row in ret_val:
            u = cls(row[1], row[2])
            u.id = row[0]
            user = f"ID: {u.id} Nazwa Użytkownika: {u.username}"
            users.append(user)

        return users

    def delete_user(self):
        if self.id is not None:
            sql = "DELETE FROM users WHERE id = %s"
            execute_sql(sql, 'workshop', self.id)
            self.id = None
            return True
        return False


class Message:
    def __init__(self, from_id, to_id, text):
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = datetime.now()
        self._id = None

    @property
    def return_id(self):
        return  self._id


    def save_to_db(self):
        if self._id is None:
            sql = 'insert into messages(from_id, to_id, text, creation_date) values (%s,%s,%s,%s) returning id;'
            ret_val = execute_sql(sql, 'workshop',self.from_id, self.to_id, self.text, self.creation_date.strftime('%Y-%m-%d %H:%M:%S'),)
            if ret_val:
                self._id = ret_val[0][0]
        else:
            sql = 'update messages set text %s where id = %s;'
            ret_val = execute_sql(sql, 'workshop', self.text, self._id)
            if ret_val:
                return True

    @classmethod
    def load_all_messages(cls):
        sql = 'select * from messages;'
        ret_val = execute_sql(sql, 'workshop')
        if ret_val:
            for message in ret_val:
                print(f'{message} \n')

    @classmethod
    def load_msg_by_id(cls, id):
        sql = 'select * from messages where id = %s;'
        ret_val = execute_sql(sql, 'workshop', id)
        if ret_val:
            print(ret_val)  # tutaj mozna przepuscic to prze cls i zrobic prypisania dla lepszej czytelnoci/ wybierlanosci
        else:
            return None

    @classmethod
    def delete_msg(cls, id):
        sql = 'select * from messages where id = %s;'
        ret_val = execute_sql(sql, 'workshop', id)
        if ret_val:
            sql = 'delete * from messages where id = %s;'

