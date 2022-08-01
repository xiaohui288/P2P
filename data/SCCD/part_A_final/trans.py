#!/usr/bin/python
# -*- coding:utf-8 -*-
import scipy.io as sio
import mat4py
import numpy as np
import os
path = 'test_data/ground_truth_mat'
save_path = 'test_data/ground_truth'
# matdata = sio.loadmat(path + "/GT_IMG_1.mat")
# print(matdata.keys())
# data = matdata["image_info"]
# 读取存放批量.nii的文件夹中的所有.nii文件的文件名
mat_filename_list = os.listdir(path)
# 批量转化 mat 文件为 txt 文件并保存在桌面的 txt_file 文件夹中
for mat_filename in mat_filename_list:
    matdata = sio.loadmat(path + '/' + mat_filename)
    data = matdata["image_info"]
    txt_filename = '/' + mat_filename[:-4] + ".txt"  # 例如将“0001.mat” 改为 “0001.txt”
    savetxt_path = save_path + txt_filename
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    np.savetxt(savetxt_path, data, fmt='%s', encoding='utf-8')   # fmt为保存格式，可不填，会以默认格式保存
print('OK')