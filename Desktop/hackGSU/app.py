from flask import Flask, render_template, request,  session, logging, url_for, redirect
from passlib.hash import sha256_crypt
import time
import  db_functions as db


app = Flask(__name__)
app.secret_key = b'\xa5\x80{\xd2\xb24\xe34xB3\xdf|\x18}\x9e'

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("signinregisterpage.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    record = db.read_password(username)
    print(record)
    if password == record[0]:
        return render_template("events.html")

    return ""

@app.route('/signup', methods=['POST'])
def signup():
    print("in signup")
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    age = request.form['age'] 
    print("Calling sign up before db")


    ## user info packet like: ( 'Ishaan', N'Australia', 'sh@gmail.com', 'Male','20','Hockey, swim, code, gym, food')
    info_packet = "'" + username + "'" + "," + "'"  + password + "'"  + "," + "'Atlanta'" + "," + "'" + email + "'" + "," + "'None'" + "," + "'"  + age + "'"  + "," + "'default'"
    print("Calling sign up", info_packet)
    db.add_user(info_packet)

    session['username'] = username    

    return render_template("interests.html")  


@app.route('/interests', methods=['POST'])
def interests():
    username = session['username']
    interest_list = ",".join(request.json['interestList'])
    print(interest_list)

    db.add_interests(username, interest_list)



    ### 
    return ""

@app.route('/get-events', methods=['POST'])
def get_events():
    event_name = request.json['eventName']
    events = {}
    records = db.get_events(event_name)
    for row in records:
        events[event_name] = row[0]
        events[location] = row[1]
        events[date_time] = row[2]
        events[num_attendees] = row[3]
        events[online_inperson] = row[4]
        events[description] = row[5]

    return events

@app.route('/get-friends', methods=['POST'])
def get_friends():
    username = request.json['username']
    return ""

if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app