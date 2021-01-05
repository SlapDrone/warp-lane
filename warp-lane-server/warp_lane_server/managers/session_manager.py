from warp_lane_server.dal.dal import DAL
from datetime import datetime
from uuid import uuid4

dal = DAL()


def check_session(session_id):
    """
    Parameters
    ==========

    session_id: string
    """
    success = False
    sql_query = f'SELECT expirytime FROM SESSIONS WHERE sessionid={session_id}'
    result = dal.run_sql(sql_query)
    if len(result) > 0:
        expiry_time = result[0][0]
        if expiry_time > datetime.utcnow():
            update_session(session_id)
            success = True
        else:
            delete_session(session_id)
    return success


def get_session_id_for_user_id(userid):
    """
    Parameters
    ==========

    userid: int

    Returns
    =======
    
    sessionid: string
    """
    sql_query = f'SELECT sessionid FROM SESSIONS WHERE userid={userid}'
    result = dal.run_sql(sql_query)
    if len(result) > 0:
        return result[0][0]
    else:
        return None


def delete_session(sessionid):
    """
    Parameters
    ==========

    sessionid: string
    """
    sql_query = 'DELETE FROM SESSIONS WHERE sessionid=%s'
    sql_params = [sessionid]
    dal.run_sql(sql_query,sql_params)


def create_session(userid):
    """
    Parameters
    ==========

    userid: int

    Returns
    =======
    
    sessionid: string
    """
    sessionid = str(uuid4())
    sql_query = f'INSERT INTO SESSIONS (sessionid, userid, expirytime) VALUES (\'{sessionid}\', {int(userid)}, current_timestamp + (20 * interval \'1 minute\'));'
    sql_result = dal.run_sql(sql_query)
    return sessionid


def update_session(sessionid):
    """
    Parameters
    ==========

    sessionid: string
    """
    sql_query = 'UPDATE SESSIONS SET expirytime= current_timestamp + (20 * interval \'1 minute\') WHERE sessionid=%s'
    sql_result = dal.run_sql(sql_query,[sessionid])
