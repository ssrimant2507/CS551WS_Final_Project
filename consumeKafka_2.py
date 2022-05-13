from utilityHelper import connectMongo, dbWrite, getKafkaConsumer

# This script consumes the tweets from kafka topic "tweets" and writes to "tweets" collection in MongoDB

consumer = getKafkaConsumer('localhost:9092', 'tweet_grp', 'tweets')
db = connectMongo('localhost', 27017)

for message in consumer:
    inputMsg = message.value
    dbWrite(db, inputMsg)
    #print(inputMsg)