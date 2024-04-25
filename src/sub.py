#MQTT Sub example

import json
import paho.mqtt.client as mqtt
import conectRedis

r = conectRedis.conectar()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(con, userdata, flags, rc, properties):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    con.subscribe("fatec/lw/dados/")

# The callback for when a PUBLISH message is received from the server.
def on_message(con, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    payload_str = msg.payload.decode('utf-8')  # decode bytes to string
    payload_json = json.loads(payload_str)  # convert string to JSON
    print("Jason TESTE:")
    print(payload_json)
    print(type(payload_json))

    
    

def conectar_sub():

    print("Running sub")
    con = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    con.on_connect = on_connect
    con.on_message = on_message

    con.connect("test.mosquitto.org", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    con.loop_forever()    