import time
import json
import paho.mqtt.client as mqtt

student_name = "Arshad Ahamed N"
unique_id = "42733010"
topic = "home/arshadahamedn-2025/sensor"

BROKER = "127.0.0.1"
PORT = 1883

def main():
    client = mqtt.Client(client_id=f"{unique_id}_publisher")

    print(f"Student Name : {student_name}")
    print(f"Register No. : {unique_id}")
    print(f"MQTT Topic   : {topic}")
    print("Connecting to MQTT broker...")

    client.connect(BROKER, PORT, keepalive=60)
    print("Connected to MQTT broker.")

    while True:
        temperature = 25
        humidity = 60
        vibration = 1  

        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "vibration": vibration
        }

        result = client.publish(topic, json.dumps(payload))

        if result.rc == 0:
            print(f"Published -> {payload}")
        else:
            print("Publish failed!")

        time.sleep(5)

if __name__ == "__main__":
    main()
