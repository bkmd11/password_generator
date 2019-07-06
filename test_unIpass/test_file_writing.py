import unittest

from unIpass_main import file_writing


class TestStorePassword(unittest.TestCase):

    # Tests ignore case feature
    def test_store_password_lower_case(self):
        dictionary = {}
        file_writing.store_password('Bank', 'abc', dictionary)

        self.assertEqual(dictionary, {'bank': 'abc'})
