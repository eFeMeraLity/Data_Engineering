import pulsar
import logging

logging.info('Connecting to Pulsar...')

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
Topic = "persistent://DEII-tenant/DEII-namespace/DEII-L1T4"
consumer = client.subscribe(Topic, subscription_name = 'DEII-L1T4-sub')

logging.info('Created consumer')

# Display message received from producer
msg = consumer.receive()
try:
    print("Received message : '%s'"%msg.data())
    # Acknowledge for receiving the message
    consumer.acknowledge(msg)
except:
    consumer.negative_acknowledge(msg)
# Destroy pulsar client
client.close()
