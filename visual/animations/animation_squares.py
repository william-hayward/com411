def run():
  def init():
    data.append({'x':[3,3,4,4,3], 'y':[3,4,4,3,3]})
    data.append({'x':[2,2,5,5,2], 'y':[2,5,5,2,2]})
    data.append({'x':[1,1,6,6,1], 'y':[1,6,6,1,1]})
  def animate(frame):
    i = frame % len(data)
    ax.cla()
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    ax.plot(data[i]['x'], data[i]['y'])

  import matplotlib.pyplot as plt
  import matplotlib.animation as animation
  global fig
  fig, ax = plt.subplots()
  data = []
  square_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 100, init_func = init)
  plt.show()
