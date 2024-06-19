#MQTT Pub example

import paho.mqtt.client as mqtt
import uuid
import time
import random
import json

def conectar_pub():
	con = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
	con.connect("test.mosquitto.org", 1883, 60)

	# Blocking call that processes network traffic, dispatches callbacks and
	# handles reconnecting.
	# Other loop*() functions are available that give a threaded interface and a
	# manual interface.
	con.loop_start()

	print("Running pub")
 
	while True:
		data=[{"uuid":"5f9edbe1-35c6-4925-a330-fd8cfa623cf7","station_description":"Jacarei","unix":int(time.time()),"parametros":{"Temperatura":round(random.uniform(28,29),2),"Umidade":round(random.uniform(30,60),2),"Vento":round(random.uniform(3,8), 2),}}]
  
		json_data = data[0]
		print(json_data)

		con.publish("fatec/lw/dados/",str(json_data))
		time.sleep(60)

conectar_pub()