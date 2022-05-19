# Import 
import adi
import sys
from os import system
from time import asctime, sleep

# Optionally pass URI as command line argument,
# Else use default context manager search
# my_uri = sys.argv[1] if len(sys.argv) >= 2 else None
my_uri = "ip:169.254.158.120" # Allan's RPI4

# Clear Screen
_ = system("cls") # For Windows only; change to "clear" for Linux and Mac

print("uri: " + str(my_uri) + "\n")

# Setup ADT75
my_temp_sensr = adi.lm75(uri=my_uri)
my_temp_sensr.max = my_temp_sensr.to_millidegrees(80.0)
my_temp_sensr.max_hyst = my_temp_sensr.to_millidegrees(75.0)


# Check Settings
print("Checking current settings...\n")
print("Update interval: " + str(my_temp_sensr.update_interval))
print("Max Threshold: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max)))
print("Max Hysteresis: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max_hyst)))

# Start Measurement Loop
print("\nNow reading temperature data every 15 secs. This test will take a while. Why don't you come back tomorrow?\n")
print("Temperature (Raw): \tTemperature (Celsius): \t\tTimestamp: ")

for i in range(5760):
	try:
		print(str(my_temp_sensr.input) + "\t\t\t" + str(my_temp_sensr.to_degrees(my_temp_sensr.input)) + "\t\t\t\t" + asctime())
		sleep(15)
	
	except:
		print("\nOH SNAP! THE SCRIPT FAILED TO GET THE MEASUREMENT VALUE AT " + asctime() + "!\n")
		break
		
del my_temp_sensr
