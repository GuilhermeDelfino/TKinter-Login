class UserModel:
    
    def setEmail(self, email: str):
        self.email = email
        
    def setPassword(self, password:str):
        self.password = password

    def getEmail(self)->str:
        return self.email
    
    def getPassword(self)->str:
        return self.password        
    
 