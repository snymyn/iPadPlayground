import time

print("Start with Enter. Stop by Cntrl-C")
print("") # Enter
start_time = time.time()
last_time = start_time

lap_num = 1

# lap time
try:
	while True:
		input()
		now = time.time()
		lap_time = round(now - last_time, 2)
		total_time = round(now - start_time, 2)
		print("lap #{}: {}({})".format(lap_num, total_time,lap_time), end = "")
		lap_num += 1
		lap_time = now #Reset laptime
except KeyboardInterrupt:
	#Ctrl-c
	print("\nEnd")
