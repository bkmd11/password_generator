import unittest
from unittest.mock import patch

from unIpass_main import password_options


# This will test my master_password() function.
# I should figure out how to make it not need my usb
class TestMasterPassword(unittest.TestCase):

    @patch('password_options.master_password', return_value='spam')
    def test_correct_password(self):


