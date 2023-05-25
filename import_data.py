import os
from skimage import io
import pandas as pd

def import_data(label_name='test'):
    """Load images and labels for train and test set from selected directories"""
    images = []
    labels = []
    
    img_files = [img for img in sorted(os.listdir(label_name)) if img.endswith('.jpg')] # image files sorted in ascending order
    label_file = os.path.join('labels', 'list_label_'+label_name+'.txt') # label file corresponding to train or test
    for img in img_files:
      images.append(io.imread(os.path.join(label_name, img)))
    df = pd.read_csv(label_file, header=None, delimiter=r"\s+")
    df = df.sort_values(0) # sort (in ascending order) label dataframe by first column which are img names
    labels = df.iloc[:, 1].tolist()
    return images, labels