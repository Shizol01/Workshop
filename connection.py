import psycopg2



connection_info = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'coderslab',
    'database': 'postgres'
}

def execute_sql(sql, database = None, *vars):
    if database is not None:
        connection_info['database'] = database
    cnx = psycopg2.connect(**connection_info)
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(sql, vars)
    try:
        return cursor.fetchall()
    except psycopg2.ProgrammingError:
        return None
    finally:
        cursor.close()
        cnx.close()


sql = "delete from users where id > 25"
execute_sql(sql, 'workshop')