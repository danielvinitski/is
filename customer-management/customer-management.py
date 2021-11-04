from kafka import KafkaConsumer
from json import loads, dumps
import threading
import flask
from pymongo import MongoClient
import os
import time

# Get Environment variables
mongodb_endpoint = "localhost:27017"
if "MONGODB_ENDPOINT" in os.environ:
    mongodb_endpoint = os.environ.get('MONGODB_ENDPOINT')
mongodb_db = "shop"
if "MONGODB_DB" in os.environ:
    mongodb_db = os.environ.get('MONGODB_DB')

kafka_endpoint = "localhost:9093"
if "KAFKA_ENDPOINT" in os.environ:
    kafka_endpoint = os.environ.get('KAFKA_ENDPOINT')
kafka_topic = "buy"
if "KAFKA_TOPIC" in os.environ:
    kafka_topic = os.environ.get('KAFKA_TOPIC')
kafka_group_id = "my-group"
if "KAFKA_GROUP_ID" in os.environ:
    kafka_group_id = os.environ.get('KAFKA_GROUP_ID')

server_port = "5005"
if "SERVER_PORT" in os.environ:
    server_port = os.environ.get('SERVER_PORT')

client = MongoClient(mongodb_endpoint)
collection = client[mongodb_db].buy

time.sleep(5)
consumer = KafkaConsumer(
    kafka_topic,
     bootstrap_servers=[kafka_endpoint],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=kafka_group_id,
     value_deserializer=lambda x: loads(x.decode('utf-8')))


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>IS Store</h1>
<p>/api/v1/getBuyList to get all buy list</p>
'''

# A route to return all purchases.
@app.route('/api/v1/getBuyList', methods=['GET'])
def get_all_buy_list():
    all_buys = []
    cursor = collection.find({})
    for document in cursor:
        if '_id' in document:
            del document['_id']
        all_buys.append(document)
    return dumps(all_buys)


def kafka_consumer():
    for message in consumer:
        message = message.value
        collection.insert_one(message)
        print('{} added to {}'.format(message, collection))


# start kafka_consumer thread
t = threading.Thread(target=kafka_consumer)
t.start()

# start flask api server
app.run(port=server_port, host='0.0.0.0')
