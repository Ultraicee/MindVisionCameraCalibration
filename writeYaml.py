#!/usr/bin/env python
# coding: utf-8
import sys

import scipy.io as io
import cv2
import numpy as np
np.set_printoptions(precision=8, suppress=True)  # 取消科学计数法

data = io.loadmat('CameraParams.mat')  # 加载镜头数据
fs = cv2.FileStorage('camera_paras.yaml', cv2.FileStorage_WRITE)
fs.write('_mLeftRotation', data['LeftRotation'].astype("float64"))
fs.write('_mRightRotation', data['RightRotation'])
fs.write('_mLeftTranslation', data['LeftTranslation'].astype("float64"))
fs.write('_mRightTranslation', data['RightTranslation'])
fs.write('_mdisMl', data['disMl'])
fs.write('_mdisMr', data['disMr'])
fs.write('_mLeftIntrinsic', data['LeftIntrinsic'])
fs.write('_mRightIntrinsic', data['RightIntrinsic'])
fs.write('F', data['F'])

# 关闭文件
fs.release()
