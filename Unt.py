import requests
from flask import Flask, render_template
from markupsafe import Markup
import random
import mysql.connector
import configparser
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
# Import imagehash
# From simple_file_checksum import get_checksum
app = Flask(__name__)

config=configparser.ConfigParser()
configFile = 'contacts.cfg'
config.read(configFile)
database = config['database']
db=database['db']
dbUser=database['user']
dbPass=database['pass']
dbHost=database['host']
cnx = mysql.connector.connect(user=dbUser, password=dbPass, host=dbHost, database=db)
@app.route('/urlhash')
def url_checksum(url):
	response = requests.get(url)
	response.status()
	return hashlib.md5(response.content).hexdigest()
@app.route('/checkinghash')
def checking_hash():
	md5 = hashlib.md5()
	response = requests.get(url)
	computed_hash = hashlib.md5(response)
	combined_data = og_RESPONSE + response
	md5.update(combined_data.encode('utf-8'))
	post_hash = md5(combined_data.encode()).hexdigest()[:6]
	if computed_hash == post_hash:
    		print("Authentic RESPONSE")
	else:
    		print("Tampering detected")
# Generation
def create_hash(input_data):
    # Convert input to string if not already
    if not isinstance(input_data, str):
        input_data = str(input_data)
    
    # Create md5 hash object
    hash_object = hashlib.md5()
    hash_object.update(input_data.encode('utf-8'))
    return hash_object.hexdigest()

	
# Verification
received_RESPONSE = "This is my authentic post..."
received_hash = received_RESPONSE.split("Checksum: ")
og_RESPONSE = received_RESPONSE.split("\nChecksum: ")
new_hash = hashlib.md5((og_RESPONSE + secret).encode()).hexdigest()[:6]
assert new_hash == received_hash  # Fails if content or secret mismatch
Post = f"{content}\nCHECKSUM: {simple_hash}"
