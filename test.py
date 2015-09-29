import unittest

from main import ValidateAccount
from main import AccountSqlite
from main import Hash

class TestValidator(unittest.TestCase):        
    def test_validate_valid_passwd(self):
        account_db = AccountSqlite()  # 1.real DB? 2. Instantiate
        passwd_hash = Hash()
        validator = ValidateAccount(account_db, passwd_hash)
        self.assertTrue(validator.check_account('kent', '123'))
        
    def test_validate_invalid_passwd(self):
        account_db = AccountSqlite()
        passwd_hash = Hash()
        validator = ValidateAccount(account_db, passwd_hash)
        self.assertFalse(validator.check_account('kent', '1234'))
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)