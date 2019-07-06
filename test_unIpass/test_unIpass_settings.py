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


# Tests my edit_name() function
class TestEdit(unittest.TestCase):

    # Tests that it changes a dictionary key
    def tests_edit_name_works(self):
        result = unIpass_settings.edit_name('bank', 'td bank', {'bank': 'abc'})

        self.assertEqual(result, {'td bank': 'abc'})

    # Tests what happens if account isnt in the dictionary
    def tests_edit_name_does_nothing_if_key_doesnt_exist(self):
        with self.assertRaises(KeyError):
            result = unIpass_settings.edit_name('eggs', 'spam', {'bank': 'abc'})
