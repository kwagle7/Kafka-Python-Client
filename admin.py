#kwagle

# Importing necessary classes from kafka.admin module
from kafka.admin import KafkaAdminClient, NewTopic

# Creating a KafkaAdminClient instance to administer Kafka topics
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# Initializing an empty list to hold NewTopic instances
topic_list = []

# Creating a NewTopic instance named 'bankbranch' with specific configurations
new_topic = NewTopic(name="bankbranch", num_partitions=2, replication_factor=1)

# Appending the newly created topic to the topic_list
topic_list.append(new_topic)

# Using the admin_client to create the specified topics (in this case, 'bankbranch')
admin_client.create_topics(new_topics=topic_list)
