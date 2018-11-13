import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm

label_warp = {'norm': 0,
              'defect1': 1,
              'defect2': 2,
              'defect3': 3,
              'defect4': 4,
              'defect5': 5,
              'defect6': 6,
              'defect7': 7,
              'defect8': 8,
              'defect9': 9,
              'defect10': 10,
              'defect11': 11,
              'defect12': 12,
              'defect13': 13,
              'defect14': 14,
              'defect15': 15,
              'defect16': 16,
              'defect17': 17,
              }

# train data
data_path = '../data'
img_path, label = [], []
for first_path in os.listdir(data_path):
    defect_label = first_path
    first_path = osp.join(data_path, first_path)
    if 'guangdong_round1_test_a_20180916' not in first_path:
        print(defect_label) 
        for img in os.listdir(first_path):
            img_path.append(osp.join(first_path, img))
            label.append(defect_label)

label_file = pd.DataFrame({'img_path': img_path, 'label': label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('../data/label.csv', index=False)


