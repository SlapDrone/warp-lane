import psycopg2

class dal():

    def __init__(self):
        self.conn = psycopg2.connect(
        dbname="warp-lane-app", 
        host="0.0.0.0", 
        port="5432", 
        user="admin", 
        password="secret")

    def run_sql(self, sql_query):

        cur = self.conn.cursor()
        cur.execute(sql_query)
        records = cur.fetchall()
        cur.close()

        return records

if __name__ == "__main__":
    dal = dal()
    records = dal.run_sql("SELECT * FROM users")
    print(records)
