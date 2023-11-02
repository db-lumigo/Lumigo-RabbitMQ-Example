import pika
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RabbitMQConsumer:

    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def start_consuming(self):
        self.channel.basic_consume(queue='hello', on_message_callback=self.callback, auto_ack=True)
        logger.info(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        logger.info(f" [x] Received {body}")

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    logger.info("Consumer started")
    consumer = RabbitMQConsumer(host='rabbitmq-service')
    try:
        consumer.start_consuming()
    except KeyboardInterrupt:
        logger.info("Consumer interrupted by user. Exiting...")
    finally:
        consumer.close()
        logger.info("Consumer ended")
