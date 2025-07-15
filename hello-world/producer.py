import pika
import sys

# connect to RabbitMQ on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue named 'hello'
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"

# send a message to the 'hello' queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(f" [x] Sent '{message}'")
connection.close()
