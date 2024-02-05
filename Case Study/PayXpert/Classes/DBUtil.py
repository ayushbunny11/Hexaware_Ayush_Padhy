from mysql.connector import connect


class DBUtil:
    def __init__(self, host, user, password, port, database):
        self.connection = connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.cursor = self.connection.cursor()

    def executeQuery(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"Query Execution Error! {e}")
            self.connection.rollback()

    def fetchAll(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Couldn't fetch all data! {e}")
            self.connection.rollback()

    def fetchOne(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Couldn't fetch one data! {e}")
            self.connection.rollback()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()