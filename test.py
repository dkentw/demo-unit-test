import unittest

from main import ValidateAccount
from main import AccountSqlite
from main import Hash

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
    def test_validate_valid_passwd(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash()
        validator = ValidateAccount(account_db, passwd_hash)
        self.assertTrue(validator.check_account('kent', '123'))
        
    def test_validate_invalid_passwd(self):
        account_db = StubAccountDB()
        passwd_hash = StubHash2()
        validator = ValidateAccount(account_db, passwd_hash)
        self.assertFalse(validator.check_account('kent', '1234'))
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)