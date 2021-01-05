from unittest import TestCase
import warp_lane_server.managers.user_manager as um
from uuid import UUID


class TestUserManager(TestCase):

    def setUp(self):
        self.sessionid = um.login("admin", "secret")
        self.assertTrue(len(self.sessionid) > 10)

    def test_create_delete_user(self):
        um.create_user("test", "password", "test@test.com")
        result = um.get_user("test")
        self.assertEqual(result[2], "password")
        um.delete_user("test")

    def tearDown(self):
        um.logout(self.sessionid)
