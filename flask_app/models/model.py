from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    def __init__(self, data):
        

        @classmethod
        def create_email(cls, data):
            query = """
                    INSERT INTO emails
                        (email)
                    VALUES
                        (%(email)s);
                    """
            return connect_to_mysql(DATABASE).query_db(query, data)

        
        @staticmethod
        def validate(data):
            is_valid = True
            if len(data['email']) < 1:
                is_valid = False
                flash("Email is required!")
            
            return is_valid
