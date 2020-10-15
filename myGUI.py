# My GUI for USRP experiments

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from myConstants import *

fvals = np.linspace(-fs/2, fs/2, hrf * ns)

# Init all plots
fig, (ax00,ax10) = plt.subplots(2,1)
# I/Q plot
(mplt0i, mplt0q) = ax00.plot(np.arange(ns), np.zeros(ns),np.arange(ns), np.zeros(ns))
# DSP scope
(mplt0s,) = ax10.plot(np.arange(ns), np.zeros(ns))

ax00.set_ylabel('I/Q')
ax00.grid(True)
ax00.set_ylim(-1,1)

ax10.set_xlim(0, 100)
ax10.set_ylim(-180,180)
ax10.grid(True)

plt.draw()
plt.pause(0.01)

def refresh():

    ax00.draw_artist(ax00.patch)
    ax00.draw_artist(mplt0i)
    ax00.draw_artist(mplt0q)
    ax10.draw_artist(ax10.patch)
    ax10.draw_artist(mplt0s)

    # ax00.relim()
    # ax00.autoscale_view()
    # ax10.relim()
    # ax10.autoscale_view()

    fig.canvas.update()
    fig.canvas.flush_events()

