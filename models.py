from connection import execute_sql
import psycopg2

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
            return u

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
            users.append(u)

        return users

    def delete_user(self):
        if self.id is not None:
            sql = "DELETE FROM users WHERE id = %s"
            execute_sql(sql, 'workshop', self.id)
            self.id = None
            return True
        return False