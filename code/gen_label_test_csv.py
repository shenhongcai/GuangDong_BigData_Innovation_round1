import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm


test_data_path = '../data/guangdong_round1_test_a_20180916'
all_test_img = os.listdir(test_data_path)
all_test_img.sort(key=lambda x:int(x[:-4]))
test_img_path = []

for img in all_test_img:
    if osp.splitext(img)[1] == '.jpg':
        test_img_path.append(osp.join(test_data_path, img))

test_file = pd.DataFrame({'img_path': test_img_path})
test_file.to_csv('../data/test.csv', index=False)
