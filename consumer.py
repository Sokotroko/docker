from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers='localhost:9094', auto_offset_reset='earliest')
for message in consumer:
    print(f"Recibido: {message.value.decode()}")
