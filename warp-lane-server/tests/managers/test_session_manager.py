from unittest import TestCase
import warp_lane_server.managers.session_manager as sm
from uuid import UUID


class TestSessionManager(TestCase):

    def setUp(self):
        self.userid = 1
        self.sessionid = sm.create_session(self.userid)
        self.assertTrue(len(self.sessionid) > 10)

    def test_get_sessionid_for_userid(self):
        sessionid = sm.get_sessionid_for_userid(self.userid)
        self.assertEqual(sessionid, str(self.sessionid))

    def test_update_session(self):
        sm.update_session(self.sessionid)

    def tearDown(self):
        sm.delete_session(self.sessionid)
