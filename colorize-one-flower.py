import torch
print(torch.__version__)
print(torch.cuda.is_available())
import os
import multiprocessing
from torch import autograd
from DeOldify.fastai.transforms import TfmType
from DeOldify.fasterai.transforms import *
from DeOldify.fastai.conv_learner import *
from DeOldify.fasterai.images import *
from DeOldify.fasterai.dataset import *
from DeOldify.fasterai.visualize import *
from DeOldify.fasterai.callbacks import *
from DeOldify.fasterai.loss import *
from DeOldify.fasterai.modules import *
from DeOldify.fasterai.training import *
from DeOldify.fasterai.generators import *
from DeOldify.fastai.torch_imports import *
from DeOldify.fasterai.filters import *
from pathlib import Path
from itertools import repeat
# from google.colab import drive
# from IPython.display import Image
import tensorboardX
torch.cuda.set_device(0)
plt.style.use('dark_background')
torch.backends.cudnn.benchmark=True