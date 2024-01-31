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

anim2 = anim_random_brain(cmap='YlOrBr', 
                          view='lateral', 
                          func=random_brain,
                            frames=15, 
                            fps=10, 
                            interval=200, 
                            fname=f'{IMAGE_DIR}brain2.gif', 
                            save=True)

anim3 = anim_random_brain(cmap='PuRd', 
                          view='lateral', 
                          func=random_brain,
                            frames=15, 
                            fps=10, 
                            interval=200, 
                            fname=f'{IMAGE_DIR}brain3.gif', 
                            save=True)

# plot univariate brain
uni1 = plot_univariate(rois=[12, 13, 14, 34, 35], view='lateral', cmap='YlGnBu')
plt.savefig(f'{IMAGE_DIR}brain4.png')

uni1 = plot_univariate(rois=[12, 13, 14, 34, 35], view='lateral', cmap='YlOrBr')
plt.savefig(f'{IMAGE_DIR}brain5.png')

uni1 = plot_univariate(rois=[12, 13, 14, 34, 35], view='lateral', cmap='PuRd')
plt.savefig(f'{IMAGE_DIR}brain6.png')

# plot multivariate brain
multi1 = plot_multivariate(rois=[12, 13, 14, 34, 35], view='lateral', cmap='YlGnBu')
plt.savefig(f'{IMAGE_DIR}brain7.png')

multi2 = plot_multivariate(rois=[12, 13, 14, 34, 35], view='lateral', cmap='YlOrBr')
plt.savefig(f'{IMAGE_DIR}brain8.png')


