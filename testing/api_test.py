from unittest import TestCase
from api_for_thousandeyes.API_testing_env import get_the_data

class TestFunction(TestCase):
    def test_TimeTest(self):
        username = 'noreply@thousandeyes.com'
        authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
        result = 'finished'
        self.assertEqual(get_the_data(username, authtoken), result)
    # def test_two(self):
    #     username = 'noreply@thousandeyes.com'
    #     authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    #     result = 'finished'
    #     self.assertEqual(get_the_data(username, authtoken), result)