from data_process import create_account
import pika
import time
import json

# Configure connection
connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

# Dealing with incoming data
def callback(ch, method, properties, body):
    message = body.decode("utf-8")
    if message:
        create_account(message)
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
