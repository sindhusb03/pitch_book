from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import boto3

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['DB_CONFIG'] = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'pitch_book'
}

# AWS S3 Configuration
s3 = boto3.client(
    's3',
    aws_access_key_id='AWS_ACCESS_KEY',
    aws_secret_access_key='AWS_SECRET_KEY'
)
BUCKET_NAME = 'your-s3-bucket-name'

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "API is working!"})

if __name__ == '__main__':
    app.run(debug=True)
