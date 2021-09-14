# Declaring object for database connection and handling dataset

class Connection:
    database_name = str;
    server = str;
    username = str;
    password = str;
    
    def __init__(self, server, username, password, database_name):
        self.server = server
        self.username = username
        self.password = password
        self.database_name = database_name
