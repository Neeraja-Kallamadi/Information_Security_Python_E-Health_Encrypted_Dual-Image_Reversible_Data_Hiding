## Import Required Packages
import matplotlib.pyplot as plt
import numpy as np

## Function to Plot Bar Graph
def barGraph(x,y1,y2,y3,y4,y5,y6,y7,y_avg,lab):
    ## Set Width of Bar
    bar_width = 0.1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
    colors = ['#00308F', '#0F52BA', '#6CA0DC', '#00FEFC','#50C878','#FFA52C','#FFFF00']
    labels = ['Lu et al[9]', 'Yao et al.[25]', 'Lee et al.[11]', 'Chi et al.[5]', 'Lu et al.[9]','Bharadwaj et al.[3]','Proposed Algorithm (n=5),(NZ=8)']
    ## Create Bar Graph
    ax1.bar(x - 0.3, y1, width=bar_width, align='center',color=colors[0])
    ax1.bar(x - 0.2, y2, width=bar_width, align='center',color=colors[1])
    ax1.bar(x - 0.1, y3, width=bar_width, align='center',color=colors[2])
    ax1.bar(x, y4, width=bar_width, align='center',color=colors[3])
    ax1.bar(x + 0.1, y5, width=bar_width, align='center',color=colors[4])
    ax1.bar(x + 0.2, y6, width=bar_width, align='center',color=colors[5])
    ax1.bar(x + 0.3, y7, width=bar_width, align='center',color=colors[6])
    ## Set X-Axis Label and Ticks
    ax1.set_xlabel('Test Images')
    ax1.set_xticks(x)
    ax1.set_xticklabels(lab)
    y=[0,0.5,1,1.5,2,2.5,3]
    ## Set Y-Axis Label and Ticks
    ax1.set_yticks(y)
    ax1.set_ylabel('Embedding rate(bits/pixel)')
    ## Set Legend
    ax1.legend(labels)
    ## Set Title
    ax1.set_title("Maximum Embedding Rate(bpp)")
    x = ['a','b','c','d','e','f','g']
    ## Define Colors and Labels for Each Bar
    colors = ['#00308F', '#0F52BA', '#6CA0DC', '#00FEFC','#50C878','#FFA52C','#FFFF00']
    labels = ['Lu et al[9]', 'Yao et al.[25]', 'Lee et al.[11]', 'Chi et al.[5]', 'Lu et al.[9]','Bharadwaj et al.[3]','Proposed Algorithm (n=5),(NZ=8)']
    ## Create Bar Chart
    ax2.bar(x[0], y_avg[0], color=colors[0])
    ax2.bar(x[1], y_avg[1], color=colors[1])
    ax2.bar(x[2], y_avg[2], color=colors[2])
    ax2.bar(x[3], y_avg[3], color=colors[3])
    ax2.bar(x[4], y_avg[4], color=colors[4])
    ax2.bar(x[5], y_avg[5], color=colors[5])
    ax2.bar(x[6], y_avg[6], color=colors[6])
    ## Add Legend and Labels and Title
    ax2.legend(labels)
    ax2.set_xlabel('Method')
    ax2.set_ylabel('Average Embedding Rate(bits/pixel)')
    ax2.set_title('Maximum Average Embedding Rate')
    ## Remove X-axis Labels
    ax2.set_xticklabels([])
    ## Display the Chart
    plt.show()
