from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss!"

def test():
	return "My code is working! "

@app.route('/login', methods=['POST'])
def create_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('wrong password')
	return home()

if __name__ == "__main__":
	## host meaning - Address of the computer and its port. Website or
	## the location is the client
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=8000)