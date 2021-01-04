from src.dal.dal import DAL
from datetime import datetime
from uuid import uuid4

dal = DAL()


def check_session(sessionid):
    success = False
    sql_query = f'SELECT "EXPIRYTIME" FROM SESSIONS WHERE "SESSIONID"={sessionid}'
    result = dal.run_sql(sql_query)
    if len(result) > 0:
        expirytime = result[0][0]
        if expirytime > datetime.utcnow():
            update_session(sessionid)
            success = True
        else:
            delete_session(sessionid)
    return success


def get_sessionid_for_userid(userid):
    sql_query = f'SELECT "SESSIONID" FROM SESSIONS WHERE "USERID"={userid}'
    result = dal.run_sql(sql_query)
    if len(result) > 0:
        return result[0][0]
    else:
        return None


def delete_session(sessionid):
    sql_query = f'DELETE FROM SESSIONS WHERE "SESSIONID"={sessionid}'
    sql_params = [sessionid]
    dal.run_sql(sql_query)


def create_session(userid):
    sessionid = uuid4()
    sql_query = f'INSERT INTO SESSIONS ("SESSIONID", "USERID", "EXPIRYTIME") VALUES (\'{sessionid}\', {int(userid)}, current_timestamp + (20 * interval \'1 minute\'));'
    sql_result = dal.run_sql(sql_query)
    return sessionid


def update_session(sessionid):
    sql_query = f'UPDATE SESSIONS SET "EXPIRYTIME"= current_timestamp + (20 * interval \'1 minute\') WHERE "SESSIONID"={sessionid}'
    sql_result = dal.run_sql(sql_query)


if __name__ == "__main__":
    val = check_session(1)
