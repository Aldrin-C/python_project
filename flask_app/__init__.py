from flask import Flask
app = Flask(__name__) 
app.secret_key = "hello" 
DATABASE = "pyproject1_db"