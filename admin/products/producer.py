import pika

params = pika.URLParameters(
    'amqps://oiefjple:zAZqZDMQVQMtX9xK6IwbGgf60D7qXJsy@squid.rmq.cloudamqp.com/oiefjple')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
