from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9094')
producer.send('test', b'Hola Mundo')
producer.flush()
