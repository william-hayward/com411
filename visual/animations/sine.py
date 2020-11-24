def run():
  def animate(frame):
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = np.arange(0, frame)
    y = np.sin(x * (np.pi/180))
    ax.plot(x, y, 'ro')


  import matplotlib.pyplot as plt
  import matplotlib.animation as animation
  import numpy as np

  fig, ax = plt.subplots()
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 10)
  plt.show()

