import torch
from torch.utils.data import Dataset
import pandas as pd
from PIL import Image,ImageDraw
import os
import ast

class PlaneDataset(Dataset):
    """Plane Dataset"""

    def __init__(self, annotations_csv, images_dir, transform = None, target_transform = None):
        # bbox will have to be fixed
        #self.bbox = np.genfromtxt(annotations_csv, delimiter=',', dtype=None, names=True, encoding=None)
        self.annotations = pd.read_csv(annotations_csv)
        self.images_dir = images_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return self.annotations.shape[0]
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.images_dir,self.annotations.iloc[idx]["image_id"])
        image = Image.open(img_path)
        geometry = ast.literal_eval(self.annotations.iloc[idx]["geometry"])
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            geometry = self.target_transform(geometry)
        return image, geometry

if __name__ == "__main__":
    dataset = PlaneDataset("data/planes_satellite/annotations.csv", "data/planes_satellite/images")
    print(dataset[0])