import pulsar
import logging

logging.info('Connecting to Pulsar...')

# Create a pulsar client by supplying ip address and port
client = pulsar.Client("pulsar://localhost:6650")

# Create a producer on the topic that consumer can subscribe to
Topic = "persistent://DEII-tenant/DEII-namespace/DEII-L1T4"
producer = client.create_producer(Topic)

logging.info('Connected to Pulsar')


def conversion(substring, operation):
    """
    A conversion function which takes a string as an input and outputs a converted string
    Args:
        substring (String)
        operation (function): This is an operation on the given input
    Returns:
        [String]: Converted String
    """

    # returns the conversion applied to input
    return function(substring)


def function(string):
    """
    A function that performs some operation on a string. You can change the operation accordingly
    Args:
        string (String): input string on which some operation is applied
    Returns:
        [String]: string in upper case
    """
    return string.upper()


# Input string
INPUT_STRING = "I want to be capitalized"

split_string = INPUT_STRING.split(" ")

logging.info('Sending Messages ...')

# Send a message to consumer
producer.send(split_string.encode('utf-8'))

# Destroy pulsar client
client.close()