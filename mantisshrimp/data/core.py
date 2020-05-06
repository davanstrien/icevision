# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_data.core.ipynb (unless otherwise specified).

__all__ = ['open_img', 'show_img', 'grid']

# Cell
from ..imports import *
from ..core import *

# Cell
def open_img(fn):
    if not os.path.exists(fn): raise ValueError(f'File {fn} does not exists')
    return cv2.cvtColor(cv2.imread(str(fn)), cv2.COLOR_BGR2RGB)

# Cell
def show_img(im, ax=None, **kwargs):
    if ax is None: fig,ax = plt.subplots(**kwargs)
    ax.set_axis_off()
    ax.imshow(im)
    return ax

# Cell
def grid(f, ims, figsize=None, **kwargs):
    figsize = figsize or [7*len(ims)]*2
    fig,axs = plt.subplots(nrows=len(ims), figsize=figsize, **kwargs)
    for fn,ax in zip(ims,axs): f(fn, ax=ax)
    plt.tight_layout()