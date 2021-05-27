from flask import json
import pika

def pass_on(user_info):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', port=5672))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    message = json.dumps(user_info)

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    connection.close()
    return True
