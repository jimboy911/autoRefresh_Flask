from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def main():
  theTime = getTime()
	return render_template("AutoRefresh.html", theTime=theTime)

def getTime():
	now = datetime.now()
	ust_string = now.strftime("%m/%d/%Y %I:%M:%S %p")
	return ust_string
