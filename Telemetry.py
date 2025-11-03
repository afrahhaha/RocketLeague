#Real-Time graph plotting for various inputs from the satellie.
import matplotlib.pyplot as plt
import random
import time

#intialization of vectors
time_data=[]
temperature_data=[]
voltage_data=[]
current_data=[]

start_time=time.time()

plt.ion()
fig, ax = plt.subplots()

i=1
while i>0:
    t = time.time() - start_time
    temperature = random.uniform(20, 40)  
    voltage = random.uniform(10.0,12.0)    
    current = random.uniform(0.1, 2.0)
    
    #create new frames by appending 
    time_data.append(t)
    temperature_data.append(temperature)
    voltage_data.append(voltage)
    current_data.append(current)

    #clears the previous frame
    ax.clear()
    ax.plot(time_data, temperature_data, label='Temperature')
    ax.plot(time_data, voltage_data, label='Voltage ')
    ax.plot(time_data, current_data, label='Current ')

    ax.legend()
    ax.set_xlabel('Time')
    ax.set_ylabel('Values')

    plt.pause(0.5)  # Pause for 0.5 seconds before next update
    i=i+1
    continue