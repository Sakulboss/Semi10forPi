import Adafruit_DHT
import board
import os
import numpy as np
import time


def read_and_save_dht_sensors(gpio_pins):
	DHT_SENSOR = Adafruit_DHT.DHT22
	temps = []

	for sensor_id, pin in enumerate(gpio_pins):
		humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, pin)
		if temperature is not None:
			current_time = time.strftime("%Y-%m-%d %H:%M:%S")
			temps.append((current_time, temperature, sensor_id + 1))
		else:
			print(f"Fehler beim Auslesen des Sensors für Bienenstock {sensor_id + 1}.")
	save_temp(temps)

def save_temp(temps):
	output_dir = "temperature_data"
	os.makedirs(output_dir, exist_ok=True)

	for time, temp, sensor_id in temps:
		data = np.array([[time, temp]])
		file_name = os.path.join(output_dir, f"{sensor_id}.csv")
		if os.path.exists(file_name):
			with open(file_name, "a") as f:
				np.savetxt(f, data, delimiter=",", fmt="%s")
		else:
			np.savetxt(file_name, data, delimiter=",", fmt="%s", header="time, temp", comments=" ")
		print(f"Gespeichert: {file_name}")

if __name__ == '__main__':
	while True:
		gpio_pins = [25, 7, 5, 6, 8]  # Beispiel GPIO-Pins für die DHT-Sensoren
		print(read_and_save_dht_sensors(gpio_pins))
		read_and_save_dht_sensors(gpio_pins)
		time.sleep(5)