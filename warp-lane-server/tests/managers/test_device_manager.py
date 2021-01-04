from unittest import TestCase
import src.managers.device_manager as dm

class TestDeviceManager(TestCase):

    def setUp(self):
        pass


    def test_insert_update_retrieve(self):
        device = '{"name": "Test", "controls": ["A", "B"]}'
        dm.insert_device_config(1,'test device', device)
        device = '{"name": "Test", "controls": ["A", "B", "C"]}'
        dm.update_device_config(1,1,json=device)
        result = dm.retrieve_devices(1)
        print(result)
        self.assertTrue(result[0] == 1)

    def test__update_device_sql_builder(self):
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename='test', json=None)
        expected_sql_query = "UPDATE DEVICES SET lastmodifiedby = 1, datemodified = current_timestamp, devicename = %s WHERE deviceid = 1"
        expected_sql_params = ['test']
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)


        device = '{"name": "Test", "controls": ["A", "B"]}'
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename=None, json=device)
        expected_sql_query = "UPDATE DEVICES SET lastmodifiedby = 1, datemodified = current_timestamp, jsonconfigtemplate = %s WHERE deviceid = 1"
        expected_sql_params = [device]
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)


        device = '{"name": "Test", "controls": ["A", "B"]}'
        name = "test"
        sql_query, sql_params = dm._update_device_sql_builder(1, 1, devicename=name, json=device)
        expected_sql_query = "UPDATE DEVICES SET lastmodifiedby = 1, datemodified = current_timestamp, devicename = %s, jsonconfigtemplate = %s WHERE deviceid = 1"
        expected_sql_params = [name, device]
        self.assertEqual(sql_query, expected_sql_query)
        self.assertEqual(sql_params, expected_sql_params)