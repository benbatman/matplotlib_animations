import matplotlib.pyplot as plt
import matplotlib.pyplot
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


t0=0
t_end=10
dt = 0.02
t = np.arange(t0,t_end+dt,dt)


#Using spherical coordinates to create the orbits
#f in [Hz]
#rho in [m]
#phi in [rad]
#alpha in [rad]

#Red orbit (1st orbit)
rho1=3
f1=1
alpha1=0
phi1=2*np.pi*f1*t
x_red = rho1*np.sin(phi1)*np.cos(alpha1)
y_red = rho1*np.sin(phi1)*np.sin(alpha1)
z_red = rho1*np.cos(phi1)

#Green orbit (2nd orbit)
rho2=3
f2=1
alpha2=np.pi/2
phi2= 2*np.pi*f2*t
x_green = rho2*np.sin(phi2)*np.cos(alpha2)
y_green = rho2*np.sin(phi2)*np.sin(alpha2)
z_green = rho2*np.cos(phi2)

#Blue orbit (3rd orbit)
rho3=3
f3=1
alpha3=2*np.pi*f3*t
phi3=np.pi/2+0*t
x_blue = rho3*np.sin(phi3)*np.cos(alpha3)
y_blue = rho3*np.sin(phi3)*np.sin(alpha3)
z_blue = rho3*np.cos(phi3)

##### ANIMATION #####

frame_amount=len(t)

#function that is animated
def update_plot(num):
    print(num)

    if t[num] < 1:
        red_orbit.set_data(x_red[0:num],y_red[0:num])
        red_orbit.set_3d_properties(z_red[0:num])

        green_orbit.set_data(x_green[0:num],y_green[0:num])
        green_orbit.set_3d_properties(z_green[0:num])

        blue_orbit.set_data(x_blue[0:num],y_blue[0:num])
        blue_orbit.set_3d_properties(z_blue[0:num])
    else:
        red_orbit.set_data(x_red[num:num+50],y_red[num:num+50])
        red_orbit.set_3d_properties(z_red[num:num+50])

        green_orbit.set_data(x_green[num:num+50],y_green[num:num+50])
        green_orbit.set_3d_properties(z_green[num:num+50])

        blue_orbit.set_data(x_blue[num:num+50],y_blue[num:num+50])
        blue_orbit.set_3d_properties(z_blue[num:num+50])


    return red_orbit, green_orbit, blue_orbit

fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(1,1)

ax1=fig.add_subplot(gs[:,:],projection='3d',facecolor=(0.9,0.9,0.9))
red_orbit,=ax1.plot([],[],[],'r',linewidth=3)
blue_orbit,=ax1.plot([],[],[],'b',linewidth=3)
green_orbit,=ax1.plot([],[],[],'g',linewidth=3)
plt.xlim(-3,3)
plt.ylim(-3,3)
ax1.set_zlim(-3,3)
# plt.xticks()
# plt.yticks()
plt.xlabel("x position [m]")
plt.ylabel("y position [m]")
ax1.set_zlabel("z position [m]")
plt.grid(True)


orbit_animation = animation.FuncAnimation(fig, update_plot, frames=frame_amount,
    interval=20, repeat=True, blit=True)
plt.show()
