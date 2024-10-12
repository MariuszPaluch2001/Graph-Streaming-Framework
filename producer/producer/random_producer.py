import time
import random

from kafka import KafkaProducer
from kafka.errors import KafkaError

BOOTSTRAP_SERVER = 'localhost:9092'
TOPIC = 'greetings'
MESSAGES = 10000

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)
    
    for _ in range(MESSAGES):
        node1 = random.randint(0, 100)
        node2 = random.randint(0, 100)
        edge_weight = random.random()
        msg = f'"nodes":[{node1}, {node2}],"edges":[[{node1},{node2},'+'{'+f'"weight": {edge_weight}' + '}]]}'
        print(msg)
        future = producer.send(TOPIC, bytes(msg, 'utf-8'))
        try:
            record_metadata = future.get(timeout=10)
        except KafkaError as e:
            print(e)
            
        #time.sleep(5)