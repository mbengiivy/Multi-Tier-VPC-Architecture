
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database connection config — replace with your RDS details
DB_CONFIG = {
    'host': '<your-rds-endpoint>',
    'user': '<your-db-username>',
    'password': '<your-db-password>',
    'database': '<your-db-name>',
}

@app.route('/health')
def health():
    """Health check endpoint for the internal ALB"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/query')
def query_db():
    """Connects to Aurora MySQL and returns data"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify({'db_time': str(result[0]), 'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

