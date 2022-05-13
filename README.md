# CS551WS_Final_Project
Steps involved to execute the application (in Windows):

1.	Install Apache Kafka, MongoDB, Tableau on the machine where the application is intended to run.
2.	Navigate to the windows directory in bin folder of Kafka, and start the Zookeeper, Kafka server.
3.	Navigate to the windows directory in bin folder of Kafka , and create a Kafka topic tweets with 3 partitions
4.	Start MongoDB and create a database twitter_db using the MongoDB Compass client (GUI)
5.	Initiate the connection between MongoDB and Tableau by navigating to the bin folder of the MongoDB connector for BI.
6.	Start the Tableau after the above connection has been established.
7.	Once the above steps are performed, please run the below mentioned python scripts in 4 different command prompts.
TweetStreamer.py
consumeKafka_1.py
consumeKafka_2.py
consumeKafka_3.py
8.	Once the python scripts are executed as mentioned in the step 6, the hashtags would be stored in the MongoDb as mentioned earlier, which can be visualized in Tableau.

#Removed the authentication keys from the credentials.properties, on purpose
