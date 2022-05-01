from hashlib import md5
from database.Connection import Connection as Conn
from model.userModel import UserModel as User

class UserController:
    
    def __init__(self):
        self.conn = Conn().getConnection()

    def createUser(self, email: str, password: str):
        sql = "INSERT INTO users (email, password) VALUES (?, ?)"
        
        user = User()
        user.setEmail(email)
        user.setPassword(md5(password))
        
        values = (user.getEmail(), user.getPassword())
        
        cursor =  self.conn.cursor()
        cursor.execute(sql, values)
        
        self.conn.commit()
        if cursor.lastrowid > 0:
            cursor.close()
            return {'status_code': 201, 'message': 'Created'}
        else:
            cursor.close()
            raise Exception('Has an error creating a new user')
        
        