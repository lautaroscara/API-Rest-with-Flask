from flask import Flask #Import Flask class to creat an instance of the app.
from flask_mysqldb import MySQL #Importa MySQL class to interact with a MySQL db 

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'super'

mysql = MySQL(app)

from app import routes