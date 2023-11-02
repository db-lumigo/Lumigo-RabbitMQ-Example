import time
import pika
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def establish_connection():
    logger.info("Establishing connection to RabbitMQ...")
    return pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-service'))

def initialize_channel(connection):
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    return channel

def send_message(channel):
    while True:
        message_content = time.time()
        message = f"Hello RabbitMQ - {message_content}"
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        logger.info(f" [x] Sent '{message}'")
        time.sleep(5)

def main():
    logger.info("Producer started")
    
    connection = establish_connection()
    channel = initialize_channel(connection)

    try:
        send_message(channel)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        connection.close()
        logger.info("Producer exited")

if __name__ == "__main__":
    main()
