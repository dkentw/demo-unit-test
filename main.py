class AccountSqlite:
    def get_password(self, id):
        account = {
            'kent': 'abcd',
            'alex': 'xyz'
        }
        try:
            password = account[id]
        except:
            password = None
        return password
    
    
class Hash:
    def get_hash(self, password):
        return 'abcd' if password == '123' else None

class MobileManager:
    def send_text(self, user, msg):
        print '{0} sent a message: {1}'.format(user, msg)
    
    
class ValidateAccount:
    def __init__(self, account_db, passwd_hash, mobile_manager):
        self.account_db = account_db
        self.passwd_hash = passwd_hash
        self.mobile_manager = mobile_manager
        
    def check_account(self, id, password):
        password_by_id = self.account_db.get_password(id)
        password_by_hash = self.passwd_hash.get_hash(password)
        if password_by_id == password_by_hash:
            self.mobile_manager.send_text(id, 'Account Valid')  # send sms
            return True
        else:
            self.mobile_manager.send_text(id, 'Account Not Valid')  # send sms
            return False
            