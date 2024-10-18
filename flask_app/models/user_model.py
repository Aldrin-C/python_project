from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id  = data['id']
        self.first_name  = data['first_name']
        self.last_name  = data['last_name']
        self.email  = data['email']
        self.password  = data['password']
        self.created_at  = data['created_at']
        self.updated_at  = data['updated_at']


# -------- CREATE USER --------
    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users
                    (first_name, last_name, email, password)
                VALUES
                    (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        return connect_to_mysql(DATABASE).query_db(query, data)
    

# -------- GET EMAIL --------
    @classmethod
    def get_email(cls, email):
        data = {
            'email' : email
        }
        query = """
                SELECT * FROM users
                WHERE email = %(email)s;
                """
        result = connect_to_mysql(DATABASE).query_db(query, data)
        print ("\n ############### DID WE RETREIVE A USER?  #############", result)
        if len(result) < 1:
            return False
        return cls(result[0])


# -------- GET User ID --------
    @classmethod
    def get_id(cls, id):
        data = {
            'id' : id
        }
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        result = connect_to_mysql(DATABASE).query_db(query, data)
        print ("\n ############### DID WE RETREIVE A USER?  #############", result)
        if len(result) < 1:
            return False
        return cls(result[0])   
    

# -------- Update User --------
    @classmethod
    def update_user(cls, data):
        query = """
                UPDATE users
                SET 
                    first_name = %(first_name)s,
                    last_name = %(last_name)s,
                    email = %(email)s
                WHERE users.id = %(id)s;
                """
        return connect_to_mysql(DATABASE).query_db(query, data)

# -------- SIGNUP/LOGIN VALIDATION --------

    @staticmethod
    def validate_reg(data):
            is_valid = True

            if len(data['first_name']) < 1:
                is_valid = False
                flash("First name is required", 'reg')
            elif len(data['first_name']) < 2:
                is_valid = False
                flash("First Name must contain at least 2 characters", 'reg')

            if len(data['last_name']) < 1:
                is_valid = False
                flash("Last Name is required", 'reg')
            elif len(data['last_name']) < 2:
                is_valid = False
                flash("Last Name must contain at least 2 characters", 'reg')
            elif not str.isalpha(data['last_name']):
                is_valid = False
                flash("Last Name must contain letters only!", 'reg')

            if len(data['email']) < 1:
                is_valid = False
                flash("Invalid email address", 'reg')
            elif not EMAIL_REGEX.match(data['email']):
                flash("Invalid email address!", 'reg')
                is_valid = False
            # check if email address already exists
            else:
                email_taken = User.get_email(data['email'])
                if email_taken:
                    is_valid = False
                    flash("Sorry, the email is already taken", 'reg')

            if len(data['password']) < 1:
                is_valid = False
                flash("Please enter your password", 'reg')
            elif len(data['password']) < 8:
                is_valid = False
                flash("Password must contain at least 8 characters", 'reg')
            elif not data['password'] == data['confirm_password']:
                is_valid = False
                flash("Passwords did not match", 'reg')

            return is_valid