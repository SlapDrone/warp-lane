import psycopg2

def get_records():
    conn = psycopg2.connect(
        dbname="warp-lane-app", 
        host="0.0.0.0", 
        port="5432", 
        user="admin", 
        password="secret")

    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    records = cur.fetchall()
    return records

if __name__ == "__main__":
    records = get_records()
    print(records)
