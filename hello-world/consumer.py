import pika

# connect to RabbitMQ on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# make sure the queue exists
channel.queue_declare(queue='hello')

# define a function to process messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# subscribe the callback to the 'hello' queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
