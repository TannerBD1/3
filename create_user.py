import mysql.connector
import configparser
import hashlib
import secrets
import getpass

# Read DB config
config = configparser.ConfigParser()
config.read('configdb.cfg')
database = config['database']
db = database['db']
dbHost = database['host']
dbUser = database['user']
dbPass = database['pass']

# Connect to DB
cnx = mysql.connector.connect(user=dbUser, password=dbPass, host=dbHost, database=db)
cursor = cnx.cursor()

# Helper: Hash password with salt
def hash_password(password, salt):
    return hashlib.md5((password + salt).encode()).hexdigest()

# Prompt for user input
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# Generate salt and hash
salt = secrets.token_hex(16)
hashedpwd = hash_password(password, salt)

# Insert into DB
query = "INSERT INTO users (username, hashedpwd, pwdsalt) VALUES (%s, %s, %s)"
cursor.execute(query, (username, hashedpwd, salt))
cnx.commit()

print("User created successfully.")

# Clean up
cursor.close()
cnx.close()
