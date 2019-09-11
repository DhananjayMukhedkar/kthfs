#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from itertools import count
from matplotlib.animation import FuncAnimation
import random
import time
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('matplotlib', 'notebook')
plt.rcParams['animation.html']='jshtml'

class Calculation:
   
    
    def lmbda(self,t):
        angle=2*np.pi*t
        result=5*np.sin(angle)
        return result
    
    def equation(self,t):
        l=self.lmbda(t)
        result=3*np.pi*np.exp(-l)
        return result
        
        
        
plt.style.use('fivethirtyeight')
x_vals=[]
y_vals=[]
fig,ax=plt.subplots()
index=count()



cal=Calculation()
def animate(i):
    x_vals.append(next(index))
    y=cal.equation(i)
    
    y_vals.append(y)    
    plt.cla()
    plt.plot(x_vals,y_vals)
   

ani = FuncAnimation(fig, animate, interval=1)
#ani.save('ex2_animation3.mp4', fps=30, extra_args=['-vcodec', 'libx264']) 

plt.tight_layout()
plt.show()
i=0




# In[ ]:




