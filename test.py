import unittest
from mock import MagicMock

from main import ValidateAccount
from main import AccountSqlite
from main import Hash
from main import MobileManager

# Stubs
class StubAccountDB:
    def get_password(self, id):
        return 'abcd'
    
    
class StubHash:
    def get_hash(self, password):
        return 'abcd'

    
class StubHash2:
    def get_hash(self, password):
        return 'abcde'
    
# Tests    
class TestValidator(unittest.TestCase):
    def setUp(self):
        mobile = MobileManager()
        self.mockMobile = MagicMock(spec=mobile)  # Mock object
        
    def test_validate_valid_passwd(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash()
        validator = ValidateAccount(account_db, passwd_hash, self.mockMobile)
        self.assertTrue(validator.check_account('kent', '123'))
        
    def test_validate_invalid_passwd(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash2()
        validator = ValidateAccount(account_db, passwd_hash, self.mockMobile)
        self.assertFalse(validator.check_account('kent', '1234'))
        
    def test_send_sms_when_account_valid(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash()
        validator = ValidateAccount(account_db, passwd_hash, self.mockMobile)
        validator.check_account('kent', '1234')
        self.mockMobile.send_text.assert_called_with('kent', 'Account Valid')  # Use mock object to assert.
        
    def test_send_sms_when_account_valid(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash2()
        validator = ValidateAccount(account_db, passwd_hash, self.mockMobile)
        validator.check_account('kent', '1234')
        self.mockMobile.send_text.assert_called_with('kent', 'Account Not Valid')  # Use mock object to assert.
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)
