# Sample Flask application
# To run the application, use the command: python app.py
# Then, navigate to http://
# localhost:5000/ in your web browser.r  

# The application will display the message: "Hi This is a sample Flask application!"
# in your web browser.
# The application is set to run in debug mode for easier development and troubleshooting.
# Make sure you have Flask installed in your Python environment.
# You can install Flask using pip:
# pip install Flask
# This application defines a single route ('/') that returns a simple string message.
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.test_database
collection = db['test_collection']
app = Flask(__name__)
@app.route('/')

def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)
    
@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    try:
        collection.insert_one(form_data)
    except Exception as e:
        return render_template('index.html', error=str(e))
    return render_template('submit.html')
if __name__ == '__main__':
    app.run(debug=True)
