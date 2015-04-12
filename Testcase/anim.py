"""
Model plot made by Melody Wolk 04/11/2015
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.misc import imread
import fnmatch
import os
import matplotlib.cm as cm

autokm = 149597871 # Convert au to kms
img = imread('space.jpg') # Background image
earth = imread('Earth.png')
moon = imread('moon.png')
# Create the plot layout
fig = plt.figure()
ax = fig.add_subplot(111)
xmin = -10
xmax = 10
ymin = -10
ymax = 10
ax.set_xlim(xmin,xmax)
ax.set_ylim(xmin,xmax)
# Set the labels for the clock
plt.text(-7.2,7.9,'2015/2115',fontsize=10,color='w')
plt.text(-8.5,8.7,'2040',fontsize=10,color='w')
plt.text(-9.7,7.9,'2065',fontsize=10,color='w')
plt.text(-8.5,7,'2090',fontsize=10,color='w')
# Display the background
plt.imshow(img, zorder=0, extent=[xmin,xmax,ymin,ymax])
# Plot the Earth at the center
plt.imshow(earth, zorder=0, extent=[-0.5,0.5,-0.5,0.5])
# Plot the Moon radius and image
ang = np.arange(0,2*np.pi, 0.01)
dTL = np.log10(384400)
plt.plot(dTL*np.cos(ang), dTL*np.sin(ang), 'w--')
plt.imshow(moon, zorder=0, extent=[dTL*np.sqrt(2)/2-0.32,dTL*np.sqrt(2)/2+0.32,dTL*np.sqrt(2)/2-0.25,dTL*np.sqrt(2)/2+0.25])
rclock = 0.5


# Find the number of files
nbfile=0
dir = '/home/melody/Downloads/nasachallenge-compact/'
list=[]
for file in os.listdir('/home/melody/Downloads/nasachallenge-compact/'):
    if fnmatch.fnmatch(file,'2015*'):
       nbfile=nbfile+1
       list.append(file)
print 'nb of files %d' % (nbfile)

# Define the reference for the clock angle
d = np.loadtxt(open(dir+list[0]))
date = d[:,0]
newdate=date-np.min(date)
thetaclock = 2*np.pi*newdate/np.max(newdate)

# Create the color table
color = cm.rainbow(np.linspace(0,1,nbfile))

# Initialize the plot
line = [ax.plot([],[],alpha=0.4, lw=1, color=color[j])[0] for j in range(nbfile)]
line.append(ax.plot([],[], lw=2, color='w')[0])

i =0
#Loop over files and create the data set
for file in list:
      d = np.loadtxt(open(dir+file))
      date = d[:,0]
      dist = d[:,1]

      newdate=date-np.min(date)
      theta = 2*np.pi*newdate/np.max(newdate)
      r = np.log10(autokm*dist)
      x=r*np.cos(theta)
      y=r*np.sin(theta)
      globals()["data"+str(i)] = np.column_stack((np.array(x),np.array(y)))
      i+=1

# Animate
def animate(num):
  for i in range(0, nbfile): 
      line[i].set_data(globals()["data"+str(i)][0:num,0], globals()["data"+str(i)][0:num,1]) 
  line[nbfile].set_data(-8+rclock*np.cos(thetaclock[0:num]), 8+rclock*np.sin(thetaclock[0:num])) 
  return tuple(line,)
       
line_ani = animation.FuncAnimation(fig, animate, interval = 0.0000001, blit=True)
plt.show()
