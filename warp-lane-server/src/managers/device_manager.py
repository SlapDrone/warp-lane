from src.dal.dal import DAL

dal = DAL()


def insert_device_config(userid, devicename, json):
    sql_query = 'INSERT INTO DEVICES (addedbyuserid, devicename, jsonconfigtemplate) VALUES (%s, %s, %s);'
    sql_params = [userid, devicename, json]
    sql_result = dal.run_sql(sql_query, sql_params)


def _update_device_sql_builder(deviceid, userid, devicename, json):
    sql_params = []
    sql_query = f'UPDATE DEVICES SET lastmodifiedby = {userid}, datemodified = current_timestamp'
    if devicename:
        sql_query += ', devicename = %s'
        sql_params.append(devicename)
    if json:
        sql_query += ', jsonconfigtemplate = %s'
        sql_params.append(json)
    sql_query += f' WHERE deviceid = {deviceid}'
    return sql_query, sql_params


def update_device_config(deviceid, userid, devicename=None, json=None):
    sql_query, sql_params = _update_device_sql_builder(deviceid, userid, devicename, json)
    sql_result = dal.run_sql(sql_query, sql_params)


def retrieve_devices(deviceid=None):
    sql_params = []
    sql_query = 'SELECT deviceid, deviceownerusername, devicename, jsonconfigtemplate FROM devicedetails_view'
    if deviceid:
        sql_params = [deviceid]
        sql_query += ' WHERE deviceid=%s'
    sql_result = dal.run_sql(sql_query, sql_params)
    return sql_result[0]