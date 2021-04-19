import pulsar

# Create a pulsar client by supplying ip address and port
client = pulsar.Client("pulsar://localhost:6650")

# Subscribe to a topic and subscription
Topic = "persistent://DEII-tenant/DEII-namespace/DEII-L1T4"
consumer = client.subscribe(Topic, "DEII-L1T4-sub")

resultant_string = ""

# Display message received from producer
try:
    while True:
        msg = consumer.receive()
        try:
            data = msg.data().decode("utf-8")
            topic = msg.topic_name()
            resultant_string += data + ' '
            # Acknowledge for receiving the message
            consumer.acknowledge(msg)
            print(f"Received ack and message: {data}")
            print(f"Topic: {topic}")
            print(f"Resultant string: {resultant_string}")
        except:
            consumer.negative_acknowledge(msg)
            print("Message failed to be processed")
finally:
    print(f"All resultant string: {resultant_string}")
    # Destroy pulsar client
    client.close()
