#MQTT Pub example

import paho.mqtt.client as mqtt
import uuid
import time
import random

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
		json =	[
					{
						"uuid": "45b37e70-28d6-409a-bd5b-da8ef275c111",  # Generate a random UUID
						"station_description": "Taubate",
						"unix": int(time.time()),  # Get the current Unix time
						"parametros": [
							{
								"Temperatura": round(random.uniform(28, 29), 2),
								"Umidade": round(random.uniform(30, 60), 2),
								"Vento": round(random.uniform(3, 8), 2),
							}
						]
					}
            	]

		msg = json

		con.publish("fatec/lw/dados/",str(msg))
		time.sleep(60)

conectar_pub()