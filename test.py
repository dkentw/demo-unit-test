import unittest

from main import ValidateAccount

class TestValidator(unittest.TestCase):        
    def test_validate_valid_passwd(self):
        self.validator = ValidateAccount()
        self.assertTrue(self.validator.check_account('kent', '123'))
        
    def test_validate_invalid_passwd(self):
        self.validator = ValidateAccount()
        self.assertFalse(self.validator.check_account('kent', '1234'))
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)