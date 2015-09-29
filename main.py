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

    
class ValidateAccount:
    def __init__(self, account_db, passwd_hash):
        self.account_db = account_db
        self.passwd_hash = passwd_hash
        
    def check_account(self, id, password):
        password_by_id = self.account_db.get_password(id)
        password_by_hash = self.passwd_hash.get_hash(password)
        if password_by_id == password_by_hash:
            return True
        else:
            return False