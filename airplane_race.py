<<<<<<< current
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

t = 0
t_end=2
dt=0.005

t = np.arange(t,t_end+dt,dt) #end time is exclusive, have to put + t_end
                             #include final time value
#Airplane 1
a1 = 400
b1 = 2
#Defining x array of size t
x1 = a1*t**b1
derivative1 = b1*a1*t**(b1-1) #speed
altitude1=2.5 # [km]
y1 = np.ones(len(t)) * altitude1

#Airplane 2
a2 = 800
b2 = 1
x2 = 800*t
derivative2 = b2*a2*t**(b2-1)
altitude2 = 2 #[km]
y2 = np.ones(len(t)) * altitude2

#Airplane 3
a3 = 200
b3 = 3
x3 = a3*t**b3
derivative3 = b3*a3*t**(b3-1)
altitude3 = 1 #[km]
y3 = np.ones(len(t)) * altitude3


#---------------- ANIMATION --------------
frame_amount = len(t)

dot1 = np.zeros(frame_amount)
n1 = 20
for i in range(0,frame_amount):
    if i==n1:
        dot1[i] = x1[i]
        n1=n1+20
    else:
        dot1[i] = x1[n1-20]

dot2 = np.zeros(frame_amount)
n2 = 20
for i in range(0,frame_amount):
    if i==n2:
        dot2[i] = x2[i]
        n2=n2+20
    else:
        dot2[i] = x2[n2-20]

dot3 = np.zeros(frame_amount)
n3 = 20
for i in range(0,frame_amount):
    if i==n3:
        dot3[i] = x3[i]
        n3=n3+20
    else:
        dot3[i] = x3[n3-20]

#Logic for plane graphic
#plane_1.set_data([x_i,x_f],y[y_i,y_f])
#In this case, y_i = y_f as altitude is constant

#if you don't want to animate a plot, don't put in this function
#Function that is iterated through with matplotlib's FuncAnimation
def update_plot(num):
    print(num)

    plane1_trajectory.set_data(dot1[0:num],y1[0:num])

    plane1_1.set_data([x1[num]-40,x1[num]+20],[y1[num],y1[num]])
    plane1_2.set_data([x1[num]-20,x1[num]], [y1[num]+0.3,y1[num]])
    plane1_3.set_data([x1[num]-20,x1[num]], [y1[num]-0.3,y1[num]])
    plane1_4.set_data([x1[num]-40,x1[num]-30], [y1[num]+0.15,y1[num]])
    plane1_5.set_data([x1[num]-40,x1[num]-30], [y1[num]-0.15,y1[num]])

    plane2_trajectory.set_data(dot2[0:num],y2[0:num])
    plane2_1.set_data([x2[num]-40,x2[num]+20], [y2[num],y2[num]])
    plane2_2.set_data([x2[num]-20,x2[num]], [y2[num]+0.3,y2[num]])
    plane2_3.set_data([x2[num]-20,x2[num]], [y2[num]-0.3,y2[num]])
    plane2_4.set_data([x2[num]-40,x2[num]-30], [y2[num]+0.15,y2[num]])
    plane2_5.set_data([x2[num]-40,x2[num]-30], [y2[num]-0.15,y2[num]])

    plane3_trajectory.set_data(dot3[0:num],y3[0:num])
    plane3_1.set_data([x3[num]-40,x3[num]+20],[y3[num],y3[num]])
    plane3_2.set_data([x3[num]-20,x3[num]], [y3[num]+0.3,y3[num]])
    plane3_3.set_data([x3[num]-20,x3[num]], [y3[num]-0.3,y3[num]])
    plane3_4.set_data([x3[num]-40,x3[num]-30], [y3[num]+0.15,y3[num]])
    plane3_5.set_data([x3[num]-40,x3[num]-30], [y3[num]-0.15,y3[num]])

    #2nd  subplot
    x_dist1.set_data(t[0:num],x1[0:num])
    x_dist2.set_data(t[0:num],x2[0:num])
    x_dist3.set_data(t[0:num],x3[0:num])

    #3rd Subplot
    speed_func_time1.set_data(t[0:num],derivative1[0:num])
    speed_func_time2.set_data(t[0:num],derivative2[0:num])
    speed_func_time3.set_data(t[0:num],derivative3[0:num])

    return plane1_trajectory, plane1_1, plane1_2, plane1_3, plane1_4,\
    plane1_5, x_dist1, plane2_trajectory,plane2_1,\
    plane3_trajectory, plane3_1, plane3_2, plane3_3, plane3_4, plane3_5,\
    plane2_2, plane2_3, plane2_4, plane2_5, x_dist2, x_dist3, speed_func_time2,\
    speed_func_time3, speed_func_time1

#facecolor defines color of the figure
fig = plt.figure(figsize=(17,10), dpi=100, facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

#Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

plane1_trajectory,=ax0.plot([],[],'r:o',linewidth=2)
plane1_1,=ax0.plot([],[],'k', linewidth=10 ) #Only control lindewidth, not length
plane1_2,=ax0.plot([],[],'k', linewidth=5)
plane1_3,=ax0.plot([],[],'k',linewidth=5)
plane1_4,=ax0.plot([],[],'k',linewidth=3)
plane1_5,=ax0.plot([],[],'k',linewidth=3)

plane2_trajectory,=ax0.plot([],[],'c:^',linewidth=2)
plane2_1,=ax0.plot([],[],'k',linewidth=10)
plane2_2,=ax0.plot([],[],'k', linewidth=5)
plane2_3,=ax0.plot([],[],'k',linewidth=5)
plane2_4,=ax0.plot([],[],'k',linewidth=3)
plane2_5,=ax0.plot([],[],'k',linewidth=3)

plane3_trajectory,=ax0.plot([],[],'y:s',linewidth=2)
plane3_1,=ax0.plot([],[],'k',linewidth=10)
plane3_2,=ax0.plot([],[],'k', linewidth=5)
plane3_3,=ax0.plot([],[],'k',linewidth=5)
plane3_4,=ax0.plot([],[],'k',linewidth=3)
plane3_5,=ax0.plot([],[],'k',linewidth=3)

#Adding subplot parameters
plt.xlim(x1[0],x1[-1]/10)
plt.ylim(0,y1[0]+0.5)
plt.xticks(np.arange(x1[0], x1[-1]+1, x1[-1]/4), size=15)
plt.yticks(np.arange(0,y1[-1]+1,y1[-1]/y1[-1]), size=15)
plt.xlabel('X-Distance', fontsize=15)
plt.ylabel('Y-Distance', fontsize=15)
plt.title('Airplane', fontsize=20)
plt.grid(True)

#Subplot 2
ax2 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist1, = ax2.plot([],[], linewidth=3, color='red', label= f'X={a1}*t^{b1}')
x_dist2, = ax2.plot([],[],linewidth=3, color = 'teal', label=f'X2={a2}*t^{b2}')
x_dist3, = ax2.plot([],[],linewidth=3, color='y', label=f'X3={a3}*t^{b3}')
# horizontal_line, = ax2.plot([],[], 'g:o', linewidth=2, label='horizontal line')
# vertical_line, = ax2.plot([],[], 'r:o', linewidth=2, label='vertical line')

#Adding subplot parameters
plt.xlim(t[0],t[-1])
plt.ylim(x1[0], x1[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x1[0],x1[-1]+1, x1[-1]/4))
plt.xlabel("Time [hrs]", fontsize=15)
plt.ylabel("x-distance [km]", fontsize=15)
plt.title("X-dstiance VS time", fontsize=15)
plt.grid(True)
plt.legend(loc='upper left', fontsize='x-large')

#Subplot 3
ax3 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed_func_time1, = ax3.plot([],[],color='red',linewidth=2,label=f'Function: deltaX/deltat = {b1*a1}*t^{b1-1}')
speed_func_time2, = ax3.plot([],[],color='teal',linewidth=2,label=f'Function: deltaX/deltat = {b2*a2}*t^{b2-1}')
speed_func_time3, = ax3.plot([],[],color='olive',linewidth=2,label=f'Function: deltaX/deltat = {b3*a3}*t^{b3-1}')

#Adding subplot parameters
plt.xlim(t[0],t[-1])
plt.ylim(derivative3[0],derivative3[-1]+1)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(derivative3[0],derivative3[-1]+1,derivative3[-1]/4))
plt.xlabel("Time in hours")
plt.ylabel("Speed [km/hr]")
plt.title('Speed as a function of time')
plt.grid(True)
plt.legend(loc='upper right')

#interval is delay between frames
#Frames is source of data to pass the update_plot function
plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount,
    interval=20, repeat=True, blit=True)
plt.show()
=======
