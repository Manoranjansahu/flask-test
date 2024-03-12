import paho.mqtt.client as mqtt
from flask import Flask, jsonify
import os
from threading import Thread

app = Flask(__name__)
mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_topic = "TEMPERATURE"
message = "a"

@app.route('/')
def index():
    global message
    return f"{message}"

def on_message(client, userdata, msg):
    global message
    message = msg.payload.decode('utf-8')

def thread():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(mqtt_broker, port = 1883)

    client.subscribe("TEMPERATURE")
    client.loop_forever()


if __name__ == '__main__':
    t1 = Thread(target = thread)
    t1.start()
    app.run(debug=True, port=os.getenv("PORT", default=5000))
