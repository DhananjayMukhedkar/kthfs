#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from itertools import count
from matplotlib.animation import FuncAnimation
import random
import time
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('matplotlib', 'notebook')
#plt.rcParams['animation.html']='jshtml'


plt.style.use('fivethirtyeight')
#plt.ylabel('Function Value')
#plt.xlabel('Time')
#plt.title('Title: {}'.format('Given Function plot'))

x_vals=[]
y_vals=[]
#fig=plt.figure()
fig,ax=plt.subplots()
#ax =fig.add_subplot(111)
#fig.show()
index=count()

def lmbda(t):
    angle=2*np.pi*t
    result=5*np.sin(angle)
    return result
    
def equation(t):
    l=lmbda(t)
    result=3*np.pi*np.exp(-l)
    return result

def animate(i):
    x_vals.append(next(index))
    y=equation(i)
    #print(y)
    #y=append(random.randint(0,5))
    y_vals.append(y)    
    plt.cla()
    plt.plot(x_vals,y_vals)
    #plt.show()

ani = FuncAnimation(fig, animate, interval=1)
#ani.save('ex2_animation.mp4') #, fps=30, extra_args=['-vcodec', 'libx264']

plt.tight_layout()
plt.show()
i=0


while False:
    x_vals.append(i)
    x = np.linspace(0, 2, 1000)
    #y=np.sin(2 * np.pi * (x - 0.01 * i))
    y=equation(i)
    y_vals.append(y)
    ax.plot(x_vals,y_vals,color='b')
    fig.canvas.draw()
    time.sleep(0.1)
    i+=1

class Calculation:
   
    
    def lmbda(self,t):
        angle=2*np.pi*t
        result=5*np.sin(angle)
        return result
    
    def equation(self,t):
        l=lmbda()
        result=3*np.pi*np.exp(-l)

def generate(t):
    #cal=Calculation()
    #print(t)
    result=cal.equation(t)
    print(result)
    
    return result







# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




