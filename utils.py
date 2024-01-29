# imports 
from nilearn import datasets, plotting
import numpy as np 
import matplotlib.pyplot as plt 
import nibabel as nib

def plot_random_matrix(min, max, size: tuple, cmap: [None or str]):
    """Plotting random matrices
    
    Parameters
    ----------
    min: int

    max: int
    
    size: tuple
    
    cmap: [None or str]

    Return
    -------
    X: ndarray
    """

    if cmap is None:
        cmap = 'viridis'

    X = np.random.uniform(low=min, high=max, size=size)
    plt.imshow(X, cmap=cmap)

    return X
