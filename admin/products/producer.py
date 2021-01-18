import pika
import json

params = pika.URLParameters(
    'amqps://oiefjple:zAZqZDMQVQMtX9xK6IwbGgf60D7qXJsy@squid.rmq.cloudamqp.com/oiefjple')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
