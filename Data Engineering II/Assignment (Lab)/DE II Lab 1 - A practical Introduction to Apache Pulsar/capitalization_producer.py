import pulsar


# Create a pulsar client by supplying ip address and port
client = pulsar.Client("pulsar://localhost:6650")

# Create a producer on the topic that consumer can subscribe to
Topic = "persistent://DEII-tenant/DEII-namespace/DEII-L1T4"
producer = client.create_producer(Topic)


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

# Send a message to consumer
for i in range(len(split_string)):
    upper_case_string = conversion(split_string[i], function)
    producer.send(upper_case_string.encode("utf-8"))

# Destroy pulsar client
client.close()