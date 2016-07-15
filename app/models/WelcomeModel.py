""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    """

    def get_user(self, id):
        query = "SELECT * from friends where id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)


    def get_all_users(self):
        query = "SELECT * from friends"
        return self.db.query_db(query)

    def add_friend(self, data):
        sql = "INSERT into friends (first_name, last_name, email, created_at, updated_at) values(:first_name, :last_name, :email, NOW(), NOW())"
        data = {'first_name': data["first_name"], 'last_name': data["last_name"], 'email': data["email"]}
        self.db.query_db(sql, data)
        return True

    def edit(self, id, data):
        query = "UPDATE friends SET first_name = :first_name, last_name= :last_name, email = :email, updated_at= NOW() Where id = :id" 
        data = { 'first_name': data['first_name'], 'last_name': data['last_name'], 'email': data["email"], 'id': id }
        self.db.query_db(query, data)
        return True

    def delete(self, id):
        query = "DELETE FROM friends WHERE id= :id"
        data = { 'id': id }
        self.db.query_db(query, data)
        return True
    """
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """