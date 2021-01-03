import psycopg2
from typing import Tuple


class DAL:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="warp-lane-app",
            host="0.0.0.0",
            port="5432",
            user="admin",
            password="secret",
        )

    def __del__(self):
        self.conn.close()

    def run_sql(self, sql_query, sql_params: Tuple = ()):
        records = []
        cur = self.conn.cursor()
        cur.execute(sql_query, sql_params)
        try:
            records = cur.fetchall()  # select vs insert this needs to be submit
        except psycopg2.ProgrammingError:
            self.conn.commit()
        cur.close()

        return records


if __name__ == "__main__":
    dal = DAL()
    records = dal.run_sql("SELECT * FROM users")
    print(records)
