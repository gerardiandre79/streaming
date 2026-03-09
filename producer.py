from kafka import KafkaProducer
import json, time

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

data = [{"text":"good"}, {"text":"bad"}]
while True:
    for d in data:
        producer.send('ml_topic', d)
    time.sleep(5)