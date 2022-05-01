from hashlib import md5
import re
from database.Connection import Connection as Conn
from model.userModel import UserModel as User

class UserController:
    
    def __init__(self):
        self.conn = Conn().getConnection()

    def createUser(self, email: str, password: str) -> dict:
        
        if not re.match('^[A-Za-z0-9]+\.[A-Za-z0-9]+@sptech.school$', email):   
            return {'status_code': 401, 'message': 'Invalid email address'}
        elif len(password) < 4:
            return {'status_code': 401, 'message': 'Password must be at least 4 characters'}
        else:
            user = User()
            user.setEmail(email)
            user.setPassword(md5(password.encode()).hexdigest())
            
            sql = "INSERT INTO users (email, password) VALUES (?, ?)"
            values = (user.getEmail(), user.getPassword())
            cursor =  self.conn.cursor()
            cursor.execute(sql, values)
            
            self.conn.commit()
            if cursor.lastrowid > 0:
                cursor.close()
                return {'status_code': 201, 'message': 'User has been created successfully'}
            else:
                cursor.close()
                return {'status_code': 500, 'message': 'Has an error to create a new user'}
        
    def login(self, email: str, password: str)->dict:
        if not re.match('^[A-Za-z0-9]+\.[A-Za-z0-9]+@sptech.school$', email):   
            return {'status_code': 401, 'message': 'Invalid email address'}
        elif len(password) < 4:
            return {'status_code': 401, 'message': 'Password must be at least 4 characters'}
        else:
            sql = "SELECT * FROM users WHERE email = ? AND password = ?"
            values = (email , md5(password.encode()).hexdigest())
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            data = cursor.fetchone()
            if data is not None:
                return {'status_code': 200, 'message': f'Welcome, your e-mail is {data[1]}! and id is {data[0]}'}
            else:
                return {'status_code': 404, 'message': 'User not found or does not exist'}
                
            
        
        