import os
import time
import glob
import datetime
import numpy as np
from w1thermsensor import W1ThermSensor, Sensor

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

#sensor_ids = ["28-030e97942eea", "28-030897941e59"]



def read_temp():
	temps = []
	for sensor in W1ThermSensor.get_available_sensors():
		sensor_id = sensor.id
		temp = sensor.get_temperature()
		time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		temps.append((time, temp, sensor_id))
	return temps

def save_temp(temps):
	output_dir = "temperature_data"
	os.makedirs(output_dir, exist_ok = True)
	for time, temp, sensor_id in temps: 
		data = np.array([[time, temp]])
		file_name = os.path.join(output_dir, f"{sensor_id}.csv")
		
		if os.path.exists(file_name):
			with open(file_name, "a") as f:
				np.savetxt(f, data, delimiter = ",", fmt = "%s")
		
		else:
			np.savetxt(file_name, data, delimiter =",", fmt = "%s", header = "time, temp", comments = " ")
		print(file_name)

while True:
	print(read_temp())
	save_temp(read_temp())
	time.sleep(5)