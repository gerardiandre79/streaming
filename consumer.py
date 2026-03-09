from kafka import KafkaConsumer
import json
from model import predict

consumer = KafkaConsumer('ml_topic', bootstrap_servers='kafka:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    text = message.value['text']
    print(predict(text))