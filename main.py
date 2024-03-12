import paho.mqtt.client as mqtt
import sys
import json

mqtt_topic = "TEMPERATURE"
mqtt_data = {"username": "admin",
          "password": "admin",
          "id": "node2",
          "value": "500"}

def on_connect(client, userdata, flags, rc, a):
    print(f"{mqtt_data['id']} Connected : {rc}")
    client.subscribe(mqtt_topic)
    data = json.dumps(mqtt_data)
    client.publish(mqtt_topic, data)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode('utf-8', 'ignore'))
    if data["id"] != mqtt_data["id"]:
        print(f"Received message on topic {msg.topic}: {data['value']}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io")

client.loop_start()

while True:
    num = input("Enter data : ")
    mqtt_data["value"] = num
    data = json.dumps(mqtt_data)
    client.publish(mqtt_topic, data)
    if num == "0":
        sys.exit(1)
