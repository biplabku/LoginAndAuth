from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "My code is working! "

if __name__ == "__main__":
	## host meaning - Address of the computer and its port. Website or
	## the location is the client
	app.run(host='0.0.0.0', port=8000)