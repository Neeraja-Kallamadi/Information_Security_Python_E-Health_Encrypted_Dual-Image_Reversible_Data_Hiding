## Import Required Packages
import matplotlib.pyplot as plt
import numpy as np

## Function to Plot Bar Graph
def scatterPlot(t,x1,y1,x2,y2,x3,y3,x4,y4):
    fig, ax = plt.subplots()
    ax.scatter(x1, y1, c = 'red',marker='^', label='Lu et al.[9]',clip_on=False) ## clip_on = False --> allows the markers to extend beyond the plot's visible area without being clipped, while setting it to True will ensure the markers are clipped to the plot's axes.
    ax.scatter(x2, y2, c = 'green',marker='*', label='Lee et al.[11]',clip_on=False)
    ax.scatter(x3, y3, c = 'blue',marker='>',label='Proposed Algorithm(n=5),(NZ=8)',clip_on=False)
    ax.scatter(x4, y4, c = 'purple',marker='*', label='Bharadwaj et al.[3]',clip_on=False)
    # Connect Consecutive Points with a Line
    ax.plot(x1, y1, '-',color = 'red')
    ax.plot(x2, y2, '-',color = 'green')
    ax.plot(x3, y3, '-',color = 'blue')
    ax.plot(x4, y4, '-',color = 'purple')
    # Set the Intervals of the X and Y Axis
    ax.set_xlim([0, 3])
    ax.set_ylim([30, 100])
    ax.legend()
    ax.set_xlabel('Embedding rate(bpp)')
    ax.set_ylabel('PSNR(dB)')
    ax.set_title(t)
    plt.show()
