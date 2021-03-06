from kafka import KafkaProducer
import json
from json import dumps
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import requests
import os
import time

# Get Environment variables
kafka_endpoint = "localhost:9093"
if "KAFKA_ENDPOINT" in os.environ:
    kafka_endpoint = os.environ.get('KAFKA_ENDPOINT')
kafka_topic = "buy"
if "KAFKA_TOPIC" in os.environ:
    kafka_topic = os.environ.get('KAFKA_TOPIC')

management_endpoint = "http://127.0.0.1:5005"
if "MANAGEMENT_ENDPOINT" in os.environ:
    management_endpoint = os.environ.get('MANAGEMENT_ENDPOINT')

server_port = "5000"
if "SERVER_PORT" in os.environ:
    server_port = os.environ.get('SERVER_PORT')

# Kafka connection initiation
time.sleep(5)
producer = KafkaProducer(bootstrap_servers=[kafka_endpoint],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return '''<h1>IS Store</h1>
<p>/api/v1/buy to buy product</p>
<p>/api/v1/getBuyList to get all buy list</p>
'''


# A route to return all of purchases.
@app.route('/api/v1/getBuyList', methods=['GET'])
@cross_origin()
def get_all_buy_list():
    r = requests.get(management_endpoint + '/api/v1/getBuyList')
    return jsonify(r.text)


# A route to create buy.
@app.route('/api/v1/buy', methods=['POST'])
@cross_origin()
def buy():
    username = str(json.loads(request.data).get('username'))
    user_id = str(json.loads(request.data).get('userId'))
    price = str(json.loads(request.data).get('price'))
    if price == 'None' or user_id == 'None' or username == 'None':
        return "wrong Body", 400
    producer.send(kafka_topic, value=json.loads(request.data))
    return jsonify()


# start flask api server
app.run(port=server_port, host='0.0.0.0')
