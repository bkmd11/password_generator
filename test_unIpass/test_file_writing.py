import unittest
import json

from unIpass_main import file_writing


class TestStorePassword(unittest.TestCase):
    """Test case for store_password"""

    def test_store_password_lower_case(self):
        """ Tests ignore case feature"""
        dictionary = {}
        file_writing.store_password('Bank', 'abc', dictionary)

        self.assertEqual(dictionary, {'bank': 'abc'})

    def test_store_password_works(self):
        """Tests that it will create a new entry"""
        dictionary = {}
        file_writing.store_password('insta', 'def', dictionary)

        self.assertIsNotNone(dictionary['insta'])

    def test_store_password_changes_stored_account(self):
        """Tests that it will update an account if it's already stored"""
        dictionary = {'spam': 'abc'}
        file_writing.store_password('spam', 'def', dictionary)

        self.assertEqual(dictionary, {'spam': 'def'})


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
