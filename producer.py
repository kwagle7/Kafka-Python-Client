#kwagle

# Importing the KafkaProducer class from the kafka library
from kafka import KafkaProducer

# Importing the json module for JSON manipulation
import json

# Creating a KafkaProducer instance with a specified value serializer that encodes values to UTF-8 encoded JSON strings
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Sending a message to the "bankbranch" Kafka topic with a dictionary payload {'atmid':1, 'transid':100}
producer.send("bankbranch", {'atmid':1, 'transid':100})

# Sending another message to the "bankbranch" Kafka topic with a different dictionary payload {'atmid':2, 'transid':101}
producer.send("bankbranch", {'atmid':2, 'transid':101})

# Flushing any messages that are buffered within the producer to ensure they are sent immediately
producer.flush()

# Closing the KafkaProducer instance, releasing resources
producer.close()
