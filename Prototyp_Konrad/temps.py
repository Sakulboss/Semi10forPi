import time
import adafruit_dht
import board
import datetime


def read_temp(pin):
    temps =[]
    dht_device = adafruit_dht.DHT22(board.D4)

    temp = dht_device.temperature
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temps.append((time, temp, pin))
    return temps


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
        print(file_name)