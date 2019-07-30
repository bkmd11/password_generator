import unittest

from unIpass_main import unIpass_settings


class TestAccountsStored(unittest.TestCase):
    """Test case for accounts_stored"""

    def test_shows_keys(self):
        """Tests that it shows keys"""
        result = unIpass_settings.accounts_stored({'bank': 'abc', 'insta': 'def'})

        self.assertEqual(list(result), ['bank', 'insta'])


class TestDelete(unittest.TestCase):
    """Tests the delete function"""
    # TODO: add tests to handle a key that isnt in dictionary
    def tests_delete_works(self):
        """Tests that it deletes from dictionary"""
        result = unIpass_settings.delete({'bank': 'abc'}, 'bank')

        self.assertEqual(len(result), 0)


class TestEdit(unittest.TestCase):
    """Tests edit_name function"""

    def tests_edit_name_works(self):
        """Tests that it chances a dictionary key"""
        result = unIpass_settings.edit_name('bank', 'td bank', {'bank': 'abc'})

        self.assertEqual(result, {'td bank': 'abc'})

    def tests_edit_name_does_nothing_if_key_doesnt_exist(self):
        """Tests what happens if account isn't in the dictionary"""
        with self.assertRaises(KeyError):
            result = unIpass_settings.edit_name('eggs', 'spam', {'bank': 'abc'})
