# imports
from utils import *
from config import IMAGE_DIR
import matplotlib.pyplot as plt 

# plot brain animation
anim1 = anim_random_brain(cmap='YlGnBu', 
                          view='lateral', 
                          func=random_brain,
                            frames=15, 
                            fps=10, 
                            interval=200, 
                            fname=f'{IMAGE_DIR}brain1.gif', 
                            save=True)

# plot univariate brain
uni1 = plot_univariate(rois=[23, 24], view='lateral', cmap='viridis')
plt.savefig(f'{IMAGE_DIR}brain2.png')

# plot multivariate brain
multi1 = plot_multivariate(rois=[21, 22, 23, 24], view='lateral', cmap='black_purple_r')
plt.savefig(f'{IMAGE_DIR}brain3.png')


