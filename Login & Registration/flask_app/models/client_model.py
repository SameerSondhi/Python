from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.controllers import clients_controller
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Client Class
class Client:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Create method for inserting new client into database
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO clients (first_name, last_name, password, email)
            VALUES (%(first_name)s, %(last_name)s, %(password)s, %(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
        
# Get client by their client.id
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM clients WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

# Get client by email
    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM clients WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

# Validator static method
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['first_name'])<2:
            flash("First name must contain 2 or more letters!", 'reg')
            is_valid = False

        if len(form_data['last_name'])<2:
            flash("Last name must contain 2 or more letters!", 'reg')
            is_valid = False

        if len(form_data['email'])<1:
            flash("Email address required!", 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            flash("Email address entered is not valid!", 'reg')
            is_valid = False
        else:
            data = {
                'email': form_data['email']
            }
            potential_client = Client.get_by_email(data)
            if potential_client:
                flash("Email already exists!", 'reg')
                is_valid = False

        if len(form_data['password'])<8:
            flash("Password must contain atleast 8 characters!", 'reg')
            is_valid = False
        elif not form_data['password'] == form_data['conf_pass']:
            flash("Passwords must match!", 'reg')
            is_valid = False

        return is_valid

