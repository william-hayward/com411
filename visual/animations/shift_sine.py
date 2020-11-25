def run():
  def animate(frame):
    ax.cla()
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    x = np.arange(0, 2*np.pi, 0.01)
    y = np.sin(x + frame / 10)#/lower number would make it faster 
    ax.plot(x, y)
    
  import matplotlib.pyplot as plt
  import matplotlib.animation as animation
  import numpy as np

  global fig
  fig, ax = plt.subplots()
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 10)
  plt.show()