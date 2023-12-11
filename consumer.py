#kwagle

# Importing the KafkaConsumer class from the kafka library
from kafka import KafkaConsumer

# Creating a KafkaConsumer instance for the 'bankbranch' topic with specific configurations
consumer = KafkaConsumer('bankbranch',
                        group_id=None,  # Setting group_id to None
                        bootstrap_servers=['localhost:9092'],  # Kafka broker address
                        auto_offset_reset='earliest')  # Setting auto offset to earliest

# Printing 'Hello' to the console
print("Hello")

# Printing information about the KafkaConsumer object (not the messages)
print(consumer)

# Iterating through messages received by the consumer indefinitely
for msg in consumer:
    # Printing the value of the received message after decoding it from bytes to UTF-8 string
    print(msg.value.decode("utf-8"))
