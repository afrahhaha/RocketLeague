#To find Altitude and Time

import numpy as np
import matplotlib.pyplot as plt  #here .pyplot needs to be used for dynamic plotting

#given
Thrust=50000 #N
g=-9.8 # m/s^2
m=1000 #kg
dt=0.1
t=np.arange(0,16.5,0.1)  #array=np.arrange(start,stop,step)

#initialize vectors
# np.zeros_like() creates a vector of same size as t
# ensure all the vectors have the saem size as t as t is the axis plotted against
h=np.zeros_like(t)    #altitude
v=np.zeros_like(t)    #velocity 
a=np.zeros_like(t)   #acceleration
v0=0
h0=0
ts=[] 
vs=[]
hs=[]

plt.ion()
fig, axs= plt.subplots(2,1)

for i in range(1,len(t)):
    if t[i]<=10:
        a[i]= Thrust/m -g
    else:
        a[i]= -g

    #now calculate v and h by integrating
    v[i] = v[i-1] + a[i]*dt
    h[i] = h[i-1] + v[i]*dt

    v0=v[i]
    h0=h[i]

    vs.append(v0)
    hs.append(h0)
    ts.append(t[i])

    #plot Velocity (vs) Time
    axs[0].clear()
    axs[0].plot(ts, vs, 'b', label='velocity')
    axs[0].legend()
    axs[0].grid(True)
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('Velocit')
    axs[0].set_title("Velocity (vs) Time")

    axs[1].clear()
    axs[1].plot(ts, hs, 'b', label='velocity')
    axs[1].legend()
    axs[1].grid(True)
    axs[1].set_xlabel('time')
    axs[1].set_ylabel('Altitude')
    axs[1].set_title("Altitude (vs) Time")
    
    plt.pause(0.1)


max_velocity=max(v)
max_alt=max(h)

print('The maximum altitude is',max_alt,'\n The maximum velocity is',max_velocity)


