import unittest
import json

from unIpass_main import file_writing


# The test case for store_password
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


class TestJsonFunction(unittest.TestCase):
    """Test case for json_function"""

    def tests_json_function_writes_data(self):
        """Tests json_function will write file in cwd"""
        file_writing.json_function('test_unIpass\\test.json', 'w', data='test_data')

        with open('test_unIpass\\test.json', 'r') as data:
            result = json.load(data)

        self.assertEqual(result, 'test_data')

    def test_json_function_reads_data(self):
        """Tests json_function will read and store data"""
        result = file_writing.json_function('test_unIpass\\test.json', 'r')

        self.assertEqual(result, 'test_data')


class TestEncryptionFunction(unittest.TestCase):
    """Test case for encryption_function"""

    def test_encrypt_function_writes_file(self):
        """Tests that the function will write a file"""
        file_writing.encrypt_function('test_unIpass\\test.encrypted', 'wb', b'test_data')
        with open('test_unIpass\\test.encrypted', 'rb') as data:
            result = data.read()

        self.assertEqual(result, b'test_data')

    def test_encrypt_function_reads_file(self):
        """Tests the function will read a file"""
        result = file_writing.encrypt_function('test_unIpass\\test.encrypted', 'rb')

        self.assertEqual(result, b'test_data')
