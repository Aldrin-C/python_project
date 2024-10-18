from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Avatar:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.attack = data['attack']
        self.health = data['health']
        self.defense = data['defense']
        self.str = data['str']
        self.vit = data['vit']
        self.type = data['type']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


# ---------- CREATE CLASS ----------
    @classmethod
    def create_class(cls, data):
        query = """
                INSERT INTO avatars
	            (name, attack, health, str, vit, defense, type, user_id)
                VALUES
	            (%(name)s, %(attack)s, %(health)s, %(str)s, %(vit)s, %(defense)s, %(type)s, %(user_id)s);
                """
        return connect_to_mysql(DATABASE).query_db(query, data)
    
    
# ---------- SHOW ALL AVATARS ----------
    @classmethod
    def get_all_avatars(cls):
        query = """
                SELECT * FROM avatars
                LEFT JOIN users
                ON avatars.user_id = users.id;
                """
        results = connect_to_mysql(DATABASE).query_db(query)
        print("XXXXXXXXXXXXXXXXX RESULTS", results)

        all_avatars = []
        for row in results:
            one_avatar = cls(row)

            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at'],
            }
            # create user and attached to one_recipe
            this_user = user_model.User(user_data)

            one_avatar.user = this_user

            all_avatars.append(one_avatar)
        return all_avatars
    


# ---------- SHOW ONE AVATAR ----------
    @classmethod
    def get_by_id(cls, id):
        data = {
            'id' : id
        }

        query = """
                SELECT * FROM avatars
                LEFT JOIN users
                ON users.id = avatars.user_id
                WHERE avatars.id = %(id)s;
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        print("XXXXXXXXXXXXXXXXX RESULTS", results)

        if results:
            this_avatar = cls(results[0])

            row = results[0]
            user_data =  {
                **row,
                'id' : row['users.id'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at'],
            }
            this_user = user_model.User(user_data)

            this_avatar.user = this_user
            return this_avatar
        return False


# ---------- DELETE AVATAR ----------
    @classmethod
    def delete_avatar(cls, data):
        query = """
                DELETE FROM avatars
                WHERE id = %(id)s;
                """

        return connect_to_mysql(DATABASE).query_db(query, data)



# ---------- VALIDATE ----------
    @staticmethod
    def validate(avatar_form):
        is_valid = True

        if len(avatar_form['name']) < 1:
            is_valid = False
            flash("Name is required!")
        elif len(avatar_form['name']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters long")

        return is_valid 