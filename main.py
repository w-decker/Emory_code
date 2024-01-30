# imports
from utils import *
from config import IMAGE_DIR

# plotting brain animation
anim1 = anim_random_brain(cmap='copper', 
                          view='lateral', 
                          func=random_brain,
                            frames=15, 
                            fps=10, 
                            interval=200, 
                            fname=f'{IMAGE_DIR}brain1.gif', 
                            save=True)



