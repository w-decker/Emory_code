# imports 
from nilearn import datasets, plotting
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def plot_mwall(cmap):
    """Plot medial wall
    Parameters
    ----------
    cmap: str
        Nilearn colormap
        
    """

    # get atlas
    atlas = datasets.fetch_atlas_surf_destrieux()

    # hemisphere
    hemi = atlas['map_left']

    # mask
    mask = np.zeros_like(hemi, dtype=float)
    roi_indices = np.where((hemi == 42) | (hemi == 23))
    mask[roi_indices] = np.random.uniform(-10, 10, size=len(roi_indices[0]))

    #fsaverage
    fsaverage = datasets.fetch_surf_fsaverage()


    p = plotting.plot_surf_roi(fsaverage['pial_left'], roi_map=mask,
                                hemi='left', view='medial',
                                bg_map=fsaverage['sulc_left'], bg_on_data=True,
                                darkness=.5, cmap=cmap)

def random_brain(frames, cmap, view):
    """Generate random brain patterns
    
    Parameters
    ----------
    cmap: str
        Nilearn colormap

    view: str
        Laterial, medial, posterior, ventral
    """

    # get axes
    plt.cla()

    # get brain info
    atlas = datasets.fetch_atlas_surf_destrieux()
    hemi = atlas['map_left']
    fsaverage = datasets.fetch_surf_fsaverage()

    #mask
    mask = np.zeros_like(hemi, dtype=float)
    mask = np.random.uniform(-10, 10, size=np.size(hemi))

    #plot 
    plot = plotting.plot_surf_roi(fsaverage['pial_left'], roi_map=mask,
                                hemi='left', view=view,
                                bg_map=fsaverage['sulc_left'], bg_on_data=True,
                                darkness=.5, cmap=cmap, figure=plt.gcf())
    
    return [plot]

def anim_random_brain(cmap, view, func, frames, fps, interval, fname: str, save: bool):
    """Animate random brain patterns"""

    plt.figure(figsize=(10, 10))
    anim = FuncAnimation(fig=plt.gcf(), func=func, frames=frames, fargs=(cmap,view,), interval=interval)

    if save:
        anim.save(f'{fname}', writer='imagemagick', fps=fps)

    return anim
