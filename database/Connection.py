import sqlite3

class Connection:
    
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.db.execute(f"""
                            {open('./database/script.sql').read()}
                        """)
        
    def getConnection(self)->sqlite3.Connection:
        return self.db