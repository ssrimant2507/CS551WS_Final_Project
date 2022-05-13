from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import dumps
from json import loads
from pymongo import MongoClient
from datetime import datetime
import re


# This Function initiates the connection with the kafka broker and return the KafkaProducer
def getKafkaProducer(host):
    return KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


# This Function initiates the connection with the kafka broker and return the KafkaConsumer,
# by subscribing to the desired topic
def getKafkaConsumer(host, groupId, topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=host,
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id=groupId,
        value_deserializer=lambda x: loads(x.decode('utf-8')))


# This Function initiates the connection with the MongoDB and return a db object
def connectMongo(myHost, myPort):
    client = MongoClient(myHost, port=myPort)
    return client.twitter_db


# This Function check is the input text is alphanumeric
def isAlphaNumericString(inputText):
    if re.match("^[a-zA-Z0-9]*$", inputText) is not None:
        return True
    return False


# This Function extracts the hashtag and stores in MongoDB
def dbWrite(db, inputMessage):
    dt_string = datetime.now().strftime("%m-%d-%Y")
    myCollection = "tweets_" + dt_string
    for word in inputMessage.split():
        if '#' in word:
            tweet_msg = word.strip()[word.strip().find('#'):]
            if tweet_msg is not None and len(tweet_msg.strip()) > 1 and isAlphaNumericString(tweet_msg[1:]):
                res = db[myCollection].update_one({"tweet_text": tweet_msg}, {"$inc": {"count": 1}}, True)
