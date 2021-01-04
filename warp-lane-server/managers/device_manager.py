from dal.dal import DAL

dal = DAL()


def insert_device_config(userid, devicename, json):
    sql_query = 'INSERT INTO DEVICES ("ADDEDBYUSERID", "DEVICENAME", "JSONCONFIGTEMPLATE") VALUES (%s, %s, %s);'
    sql_params = [userid, devicename, json]
    sql_result = dal.run_sql(sql_query, sql_params)


def update_device_config(deviceid, userid, devicename=None, json=None):
    sql_params = []
    sql_query = f'UPDATE DEVICES SET "LASTMODIFIEDBY"={userid}, "DATEMODIFIED"=current_timestamp'
    if devicename:
        sql_query += ', \"DEVICENAME\" =  %s'
        sql_params.append(devicename)
    if json:
        sql_query += ', \"JSONCONFIGTEMPLATE\" = %s'
        sql_params.append(json)
    sql_query += f' WHERE "DEVICEID" = {deviceid}'
    sql_result = dal.run_sql(sql_query, sql_params)


if __name__ == "__main__":
    device = '{"name": "Test", "controls": ["A", "B"]}'
    insert_device_config(1,'test device', device)
    device = '{"name": "Test", "controls": ["A", "B", "C"]}'
    update_device_config(1,1,json=device)