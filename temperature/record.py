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
	#print(read_temp())
	save_temp(read_temp())
	time.sleep(5)



'''
def read_temp(sensor_ids):
	temps = []
	for sensor_id in sensor_ids:
		base_dir = "/sys/bus/w1/devices/"
		device_folder = glob.glob(base_dir + "28*")[0]
		device_file = "/sys/bus/w1/devices/w1_bus_master1/" + sensor_id	+ "/temperature.txt"
		print(device_file)			
		f = open("device_file", "r")
	lines = f.readlines()
	f.close()
	print(lines)
	while lines[0].strip()[-3:] != "YES":
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find("t=")
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
	time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	temps.append((time. temp_c, sensor_id))
	return temps()

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
			np.savetxt(file_name, limiter =",", fmt = "%s", header = "time, temp", cooments = " ")

		
save_temp(read_temp(sensor_ids))


os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"

def read_temp_raw():
	f = open(device_file, "r")
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != "YES":
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find("t=")
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c

while True:
	if read_temp() > 18.0:
		print(f"{read_temp()} Viel zu heiß! Mach alle Fenster auf!")
	else:
		print(read_temp())
	time.sleep(0.5)
	
	-----------

def read_temp(sensor_ids):
	temps = []
	for sensor_id in sensor_ids:
		sensor = W1ThermSensor(sensor_id = sensor_id)
		temp = sensor.get_temperature()
		time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		temps.append((time. temp, sensor_id))
	return temps()

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
			np.savetxt(file_name, limiter =",", fmt = "%s", header = "time, temp", cooments = " ")
'''

