import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rabbit')

channel.basic_publish(exchange='',
                      routing_key='rabbit',
                      body=b'Hello from Django')

print("DONE")
connection.close()
