import collections.abc
import requests
import pytest

import warp_lane_server.text as wl_text


def nested_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = nested_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


class TestServerLogin:
    """Note: server must be running on localhost for this test suite!"""
    url = 'http://0.0.0.0:8001/login'

    username = 'admin'
    user_id = 1
    password = 'secret'

    bad_username = 'admin1'
    bad_password = 'secret1'

    # Expected behaviour.
    cases_dict = {
        'good': {
            'payload': {
                wl_text.login_param_username: username,
                wl_text.login_param_password: password,
            },
            'status_code': 200,
            'response_keys': [wl_text.login_key_session_id],
        },
        'bad_username': {
            'payload': {
                wl_text.login_param_username: bad_username,
                wl_text.login_param_password: password,
            },
            'status_code': 400,
            'response_keys': [wl_text.generic_error_key],
            'error_msg': wl_text.login_message_bad_username
        },
        'bad_password': {
            'payload': {
                wl_text.login_param_username: username,
                wl_text.login_param_password: bad_password,
            },
            'status_code': 400,
            'response_keys': [wl_text.generic_error_key],
            'error_msg': wl_text.login_message_bad_pw,
        }
    }

    # Now get responses from the server.
    responses_dict = {}
    for case, config in cases_dict.items():
        r = requests.post(url, data=config['payload'])
        responses_dict[case] = {
            'response_status_code': r.status_code,
            'response_json': r.json(),
        }

    # Update the cases dict for convenience.
    nested_update(cases_dict, responses_dict)

    @pytest.mark.parametrize('config', cases_dict.values())
    def test_login_status_code(self, config):
        """
        Test status codes expected under the cases:
        - good login
        - bad username
        - bad password
        """
        assert config['response_status_code'] == config['status_code']

    @pytest.mark.parametrize('config', cases_dict.values())
    def test_login_responses(self, config):
        """
        Test response keys are as expected under the above cases.
        """
        assert(all(
            [k in config['response_json'] for k in config['response_keys']])
        )

    @pytest.mark.parametrize('config', [cases_dict['bad_password'],
                                        cases_dict['bad_username']]
                             )
    def test_error_messages(self, config):
        assert config['error_msg'] == config['response_json']['error']
