import unittest

from unIpass_main import unIpass_settings


# Tests accounts_stored()
class TestAccountsStored(unittest.TestCase):

    # Tests shows keys
    def test_shows_keys(self):
        result = unIpass_settings.accounts_stored({'bank': 'abc', 'insta': 'def'})

        self.assertEqual(list(result), ['bank', 'insta'])


# Tests the delete function
class TestDelete(unittest.TestCase):

    # Tests that it deletes from a dictionary
    def tests_delete_works(self):
        result = unIpass_settings.delete({'bank': 'abc'}, 'bank')

        self.assertEqual(len(result), 0)
