from flask import Flask, request, redirect, render_template, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = 'the random string'

# MongoDB connection setup
MONGO_URI = "mongodb+srv://db_hdhld:j22lE8ZyPDJOUgNO@arindam.leumzc3.mongodb.net"
client = MongoClient(MONGO_URI)
db = client.get_database("arindam")
collection = db.get_collection("arindamdas")

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        name = request.form.get('name')
        value = request.form.get('value')
        
        # Insert the data into MongoDB
        collection.insert_one({"name": name, "value": value})

        # Redirect on success
        return redirect('/success')
    except Exception as e:
        flash(f"Error: {str(e)}")
        return render_template('index.html')

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)

