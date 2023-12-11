# Kafka-Python-Client
Using kafka-python to interact with Kafka server in Python. You will send and receive messages through the kafka-python client.

Download Kafka, by running the command below:
<pre>
  wget https://archive.apache.org/dist/kafka/3.5.1/kafka_2.12-3.5.1.tgz
</pre>
Extract kafka from the zip file by running the command below.
<pre>
  tar -xzf kafka_2.12-3.5.1.tgz
</pre>
Change to the kafka_2.12-3.5.1 directory.
<pre>
  Change to the kafka_2.12-3.5.1 directory.
</pre>
ZooKeeper is required for Kafka to work. Start the ZooKeeper server.
<pre>
  bin/zookeeper-server-start.sh config/zookeeper.properties
</pre>
# Start the Kafka Broker Service
Start a new terminal
Change to the kafka_2.12-3.5.1 directory.
<pre>
  cd kafka_2.12-3.5.1
</pre>
Run the commands below. This will start the Kafka message broker service.
<pre>
  bin/kafka-server-start.sh config/server.properties
</pre>

# Create a topic in the Admin.py file, Create Producer.py file, and Consumer.py file, and Execute these three python files

After creating the files add the relevant codes to each of the file.
Example is given below:
![image](https://github.com/kwagle7/Kafka-Python-Client/assets/13037108/7ed8ee6a-5996-4ff3-a72b-f857ecfb2c0f)
