import unittest

from unIpass_main import file_writing


class TestStorePassword(unittest.TestCase):

    def setUp(self):
        self.dictionary = {}

    # Tests ignore case feature
    def test_store_password_lower_case(self):
        file_writing.store_password('Bank', 'abc', self.dictionary)

        self.assertEqual(self.dictionary, {'bank': 'abc'})

    # Tests that it will create a new entry
    def test_store_password_works(self):
        file_writing.store_password('insta', 'def', self.dictionary)

        self.assertIsNotNone(self.dictionary['insta'])

# Todo: figure out tests for my other functions in file_writing
