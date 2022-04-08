import os
import pika

class Publisher:
  def __init__(self):
    self.__host = os.getenv("MQ_HOST")
    self.__port = os.getenv("MQ_PORT")
    self.__vhost = os.getenv("MQ_VHOST")
    self.__cred = pika.PlainCredentials(os.getenv("MQ_ID"), os.getenv("MQ_PW"))
    self.__queue = os.getenv("MQ_QUEUE")

    self.conn = pika.BlockingConnection(pika.ConnectionParameters(self.__host, self.__port, self.__vhost, self.__cred))

  def sendMsg(self, msg):
    chan = self.conn.channel()
    chan.basic_publish(
      exchange='',
      routing_key=self.__queue,
      body=msg
    )

if __name__ == '__main__':
  from dotenv import load_dotenv
  import json
  load_dotenv(verbose=True)

  publisher = Publisher()

  publisher.sendMsg(json.dumps({"Hello":"World"}))
