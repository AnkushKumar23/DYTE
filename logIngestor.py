from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime

app = Flask(_name_)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        data = request.get_json()
        data['@timestamp'] = datetime.utcnow().isoformat()  # Add a timestamp
        es.index(index='logs', body=data)
        return jsonify({'message': 'Log ingested successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if _name_ == '_main_':
    app.run(port=3000)