import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', 'my-subscription')

try:
    while True:
        msg = consumer.receive()
        try:
            print("Received message '%s' id='%s'", msg.data().decode('utf-8'), msg.message_id())
            consumer.acknowledge(msg)
        except:
            consumer.negative_acknowledge(msg)
finally:
    client.close()