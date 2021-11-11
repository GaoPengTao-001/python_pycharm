import pika
import json

class MQUtil:
    __user = "gaopengtao"
    __password = "gaopengtao"
    __queue = "python-test"
    __channel = None
    __connection = None
    def __init__(self):
        credentials = pika.PlainCredentials(self.__user, self.__password)  # mq用户名和密码
        # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.31.55', port=5672, virtual_host='/', credentials=credentials))
        self.__channel = self.__connection.channel()
        # 声明消息队列，消息将在这个队列传递，如不存在，则创建
        result = self.__channel.queue_declare(queue=self.__queue)

    def put_data(self,data):
        message = json.dumps(data)
        # 向队列插入数值 routing_key是队列名
        self.__channel.basic_publish(exchange='', routing_key='python-test', body=message)
        print(message)

    def __del__(self):
        self.__connection.close()
        print("销毁MQUtil")