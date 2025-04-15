#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import random
import mysql.connector
import configparser
from flask_httpauth import HTTPBasicAuth
import hashlib

app = Flask(__name__)

config=configparser.ConfigParser()
configFile = 'configdb.cfg'
config.read(configFile)
database = config['database']
db=database['db']
dbHost=database['host']
dbUser=database['user']
dbPass=database['pass']
cnx = mysql.connector.connect(user=dbUser, password=dbPass, host=dbHost, database=db)

#TODO check for xss stuff
#TODO integrate group code

def genHash(inputText):
    encoded_string = inputText.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    return md5_hash.hexdigest()

def checkUser(username, clearpass):
    cursor = cnx.cursor()
    cursor.execute("SELECT hashedpwd, pwdsalt FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    if not result:
        return False  # user not found
    
    stored_hash, salt = result
    input_hash = genHash(clearpass + salt)
    cursor.close()
    return input_hash == stored_hash





@app.route('/')
def index():
    titleText="Image Site 5000"
    bodyText=Markup("""
    <h1>Please Enter Credentials</h1>
    <br>
    </br>""")
    bodyText=bodyText + Markup("""
    <br>
    <form method="POST" action="/login">
        <label for="username">Username: </label>
        <input type="text" id="username" name="username"><br>
        <label for="pass">Password: </label>
        <input type="password" id="pass" name="pass"><br>
        <input type="submit" value="Login">
    </br>""")
    return render_template('template.html', titleText=titleText, bodyText=bodyText)




@app.route('/auth')
def auth():
    titleText = "hackoman"
    bodyText=Markup("<h1>I'm In</h1>")
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['pass']
    if checkUser(username, password):
        return redirect(url_for('auth'))
    else:
        titleText = "INVALID CREDENTIALS"
        bodyText = Markup("""
        <h1>Login failed. Invalid credentials.</h1>
                          """)
        return render_template('template.html', titleText=titleText, bodyText=bodyText)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

