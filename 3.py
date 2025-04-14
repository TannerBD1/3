


Hunter’s code:
#!/usr/bin/env python3
from flask import Flask, render_template
from markupsafe import Markup
import mysql.connector
import configparser
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

HTML ELEMENTS:
H1
Form:
Input
Button
label



app = Flask(__name__)

config=configparser.ConfigParser()
configFile = 'contacts.cfg'
config.read(configFile)
database = config['database']
db=database['db']
dbHost=database['host']
cnx = mysql.connector.connect(user=dbUser, password=dbPass, host=dbHost, database=db)

Tanners code:
Import random
str(random.randint(0,9999)0



MJ:
import requests
@app.route('/gettingImage')
def gettingImage():
    url =
    response
    image_large = response['preview'][-2]
    website = response [ board or image source]
    return image_large, board or image source

Tanner; 
import hashlib
From PIL import Image
Import imagehash
From simple_file_checksum import get_checksum

@app.route(‘/urlhash’)
Def url_checksum(url):
	Response = requests.get(url)
	response.status()
	Return hashlib.md5(response.content).hexdigest()
@app.route(‘/checkinghash’)
Def checking_hash():
md5 = hashlib.md5()
md5.update(combined_data.encode('utf-8'))
post_hash = md5(combined.encode()).hexdigest()[:6]
if computed_hash == published_hash:
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
Assert new_hash == received_hash  # Fails if content or secret mismatch
	Post = f”{content}\nCHECKSUM: {simple_hash}”
