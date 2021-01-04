from unittest import TestCase
import src.managers.user_manager as um
from uuid import UUID

class TestUserManager(TestCase):

    def setUp(self):
        self.sessionid = um.login("admin", "secret")
        self.assertTrue(len(self.sessionid)>10)

    def test_placeholder(self):
        pass

    def tearDown(self):
        um.logout(self.sessionid)