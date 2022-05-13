import tweepy
import configparser
from utilityHelper import getKafkaProducer

# Authentication keys fetched from the credentials.properties file
config = configparser.RawConfigParser()
config.read('credentials.properties')

consumer_key = config.get('CredentialSection', 'consumer_key').strip('"')
consumer_secret = config.get('CredentialSection', 'consumer_secret').strip('"')
access_token = config.get('CredentialSection', 'access_token').strip('"')
access_token_secret = config.get('CredentialSection', 'access_token_secret').strip('"')

producer = getKafkaProducer('localhost:9092')


class TweetStreamer(tweepy.Stream):

    def on_status(self, status):
        # publishing to Kafka topic "tweets"
        producer.send('tweets', value=status.text)
        print(status.id)


# Configuring the twitter stream object with the authentication keys
tweetStream = TweetStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Applying the filter to the twitter stream object to fetch the tweets containing hashtags(#),
# and pertaining to Hudson county

tweetStream.filter(track=['#'],
                   locations=[-74.166087, 40.64199, -73.984739, 40.823582],  # Hudson county
                   languages=['en'])
