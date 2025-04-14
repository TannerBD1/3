#!/usr/bin/env python3
from flask import Flask, render_template
from markupsafe import Markup
import random
import mysql.connector
import configparser
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
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

webAuth = config['httpAuth']
httpUser = webAuth['user']
httpPass = webAuth['pass']

auth = HTTPBasicAuth()
users = { httpUser : generate_password_hash(httpPass) }

#this is for megabasic http auth. we are going to do forms
# @auth.verify_password
# def verify_password(username, password):
#     if username in users and \
#         check_password_hash(users.get(username), password):
#         return username




def checkUser(username, clearpass):
    cursor = cnx.cursor()
    query = f'select hashedpwd from users where user='
    cursor.execute(query)

def genHash(inputText):
    encoded_string = inputText.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    return md5_hash.hexdigest()



@app.route('/')
def index():
    titleText="Image Site 5000"
    bodyText=Markup("""
    <h1>Please Enter Credentials</h1>
    <br>
    </br>""")
    bodyText=bodyText + Markup("""
    <br>
    <form>
        <label for="username">Username: </label>
        <input type="text" id="username" name="username"><br>
        <label for="pass">Password: </label>
        <input type="password" id="pass" name="pass"><br>
    </br>""")
    return render_template('template.html', titleText=titleText, bodyText=bodyText)




@app.route('/contacts')
def contacts():
    cursor = cnx.cursor()
    titleText = "everest legends"
    bodyText=Markup("<table><tr><td> Legends </td><td>")
    query = 'select id, CONCAT(first, " ", last) from contactsTable'
    cursor.execute(query)
    for id, name in cursor:
        newRow="<tr><td> <a href=/contactsDetail/" +str(id) + ">"
        newRow=newRow + name + "</a></td></td> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText=bodyText + Markup("</table>")
    cursor.close()
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/contactsDetail/<id>/')
def contactsDetail(id):
    cursor = cnx.cursor(prepared=True)
    query="select CONCAT(first, \" \", last), email, phone from contactsTable where id =%s"
    cursor.execute(query, (id,))
    for name, email, phone in cursor:
        name=name
        email=email
        phone=phone
    cursor.close()
    titleText="Details for " +name
    bodyText="Name: " + name + Markup("<br>")
    bodyText=bodyText + "Email: " + email + Markup("<br>")
    bodyText=bodyText + "Phone Number: " + phone + Markup("<br><a href=/> home</a>")
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

