from unittest import TestCase
import src.managers.device_manager as dm

class TestDeviceManager(TestCase):

    def __setup__(self):
        pass

    def test__update_device_sql_builder(self):
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename='test', json=None)
        expected_sql_query = "UPDATE DEVICES SET \"LASTMODIFIEDBY\" = 1, \"DATEMODIFIED\" = current_timestamp, \"DEVICENAME\" = %s WHERE \"DEVICEID\" = 1"
        expected_sql_params = ['test']
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)


        device = '{"name": "Test", "controls": ["A", "B"]}'
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename=None, json=device)
        expected_sql_query = "UPDATE DEVICES SET \"LASTMODIFIEDBY\" = 1, \"DATEMODIFIED\" = current_timestamp, \"JSONCONFIGTEMPLATE\" = %s WHERE \"DEVICEID\" = 1"
        expected_sql_params = [device]
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)


        device = '{"name": "Test", "controls": ["A", "B"]}'
        name = "test"
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename=name, json=device)
        expected_sql_query = "UPDATE DEVICES SET \"LASTMODIFIEDBY\" = 1, \"DATEMODIFIED\" = current_timestamp, \"DEVICENAME\" = %s, \"JSONCONFIGTEMPLATE\" = %s WHERE \"DEVICEID\" = 1"
        expected_sql_params = [name, device]
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)