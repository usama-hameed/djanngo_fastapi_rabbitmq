import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='rabbit')

    def callback(ch, method, properties, body):
        print("In FastAPI")
        print(body)

    print("DONE")
    channel.basic_consume(queue='rabbit', on_message_callback=callback, auto_ack=True)

    try:
        channel.start_consuming()  # Start consuming messages in a non-blocking way
    except KeyboardInterrupt:
        print('Interrupted')
        connection.close()  # Close the connection gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()
