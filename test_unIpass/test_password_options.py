import unittest

from unIpass_main import password_options


# Testing my generator() function
class TestGenerator(unittest.TestCase):

    # Tests it comes up with the n length
    def test_length(self):
        result = password_options.generator(17)

        self.assertEqual(len(result), 17)


# Testing get_password()
class TestGetPassword(unittest.TestCase):

    # Sets up my dictionary
    def setUp(self):
        self.dictionary = {'bank': 'ABC', 'insta': 'DEF', 'face': 'GHI'}

    # Tests that it finds a password when account is in dictionary
    def test_get_password_gets_password(self):
        result = password_options.get_password('bank', self.dictionary)

        self.assertEqual(result, 'ABC')

    # Tests that it ignores case of account_name
    def test_case_sensitivity(self):
        result = password_options.get_password('BANK', self.dictionary)

        self.assertEqual(result, 'ABC')

    # Tests that it will return message if password isn't in dictionary
    def test_get_password_wont_get_password(self):
        result = password_options.get_password('spam', self.dictionary)

        self.assertIsNone(result)



