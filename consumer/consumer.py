import os
import pika

class Consumer:
  def __init__(self):
    self.__host = os.getenv("MQ_HOST")
    self.__port = os.getenv("MQ_PORT")
    self.__vhost = os.getenv("MQ_VHOST")
    self.__cred = pika.PlainCredentials(os.getenv("MQ_ID"), os.getenv("MQ_PW"))
    self.__queue = os.getenv("MQ_QUEUE")

    self.conn = pika.BlockingConnection(pika.ConnectionParameters(self.__host, self.__port, self.__vhost, self.__cred))

  @staticmethod
  def on_message(channel, method_frame, header_frame, body):
    print(body.decode("utf8"))

  def consume(self):
    chan = self.conn.channel()
    chan.basic_consume(
      queue=self.__queue,
      on_message_callback=Consumer.on_message,
      auto_ack=True
    )
    print("Consumer Start")
    chan.start_consuming()

if __name__ == '__main__':
  from dotenv import load_dotenv
  load_dotenv(verbose=True)

  publisher = Consumer()

  publisher.consume()
