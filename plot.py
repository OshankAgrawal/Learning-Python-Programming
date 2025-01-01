import matplotlib.pyplot as plt
import numpy as np
import random
xpoints,ypoints = [0]*20,[0]*20
for i in range(0,20,10):
    ypointsin = i
    xpointsin = ypointsin*10 + 56
    xpoints[i] = xpointsin
    ypoints[i] = ypointsin
plt.barh(ypoints, xpoints)
plt.plot(ypoints, xpoints)
plt.show()