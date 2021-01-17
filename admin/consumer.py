import pika

params = pika.URLParameters(
    'amqps://oiefjple:zAZqZDMQVQMtX9xK6IwbGgf60D7qXJsy@squid.rmq.cloudamqp.com/oiefjple')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()
