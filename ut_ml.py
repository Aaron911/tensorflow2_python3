#!/usr/bin/env python3
"""
TF2 docker unit test package for regression testing.

Make sure all the necessary tf python packages are bueno
"""

__author__ = 'Dave Turvene'
__email__  = 'dturvene at dahetral.com'
__copyright__ = 'Copyright (c) 2019 Dahetral Systems'
__version__ = '0.1'
__date__ = '20191105'

import sys
from os import path
import unittest
from pdb import set_trace as bp

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds

def plt_setup():
    '''configure matplotlib'''
    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 10}
    matplotlib.rc('font', **font)

    plt.style.use(['ggplot'])

def ut_plt():
    '''
    plt display of images
    '''
    imgfiles=['/data/pepper.jpg', '/data/teddy-bear.jpg']

    fig = plt.figure(figsize=(8, 12))
    rows=2
    columns=1
    i=1
    for f in imgfiles:
        img = mpimg.imread(f)
        a=fig.add_subplot(rows,columns,i)
        a.set_title(f)
        i+=1
        plt.imshow(img)
    plt.tight_layout(h_pad=10.0, w_pad=10.0)
    plt.show()

def ut_sns():
    '''
    seaborn image generated by ut_br.py
    '''

    sns_pairplot_file='/tmp/ts_data.png'

    if not path.exists(sns_pairplot_file):
        print(f'{sns_pairplot_file} does not exist, need to run ut_br.py')
        return True
    
    img = mpimg.imread(sns_pairplot_file)

    plt.figure(figsize=(20., 16.))
    plt.imshow(img)
    plt.show()

def ut_tfds():
    '''
    https://www.tensorflow.org/datasets
    
    https://www.tensorflow.org/datasets/catalog/overview
    122 datasets

    lfw: https://www.tensorflow.org/datasets/catalog/lfw 
    TRAIN: 13,233
    '''
    # print(tfds.list_builders())

    ds_tra = tfds.load(name='lfw', split=tfds.Split.TRAIN)
    #ds_tst = tfds.load(name='lfw', split=tfds.Split.TEST)
    #ds_val = tfds.load(name='lfw', split=tfds.Split.VALIDATION)

    ds = ds_tra.shuffle(1024).batch(16).prefetch(tf.data.experimental.AUTOTUNE)

    fig = plt.figure(figsize=(16,16))

    # 4D conv2D layer (batch, rows, cols, channels)
    for features in ds.take(1):
        img4d = features['image']
        print('i={}, label={}'.format(img4d.shape, features['label']))
        for i in range(img4d.shape[0]):
            a = fig.add_subplot(4,4,i+1)
            plt.imshow(img4d[i])
        plt.show()

    
class Ut(unittest.TestCase):
    def setUp(self):
        plt_setup()
    def tearDown(self):
        pass
    #@unittest.skip('good')
    def test1(self):
        ut_plt()
    #@unittest.skip('good')
    def test2(self):
        ut_sns()
    #@unittest.skip('good')
    def test3(self):
        ut_tfds()

if __name__ == '__main__':
    # exec(open('dt_ut.py').read())
    print(f'python ver={sys.version}')
    print(f'numpy ver={np.__version__}')
    print(f'seaborn ver={sns.__version__}')
    print(f'matplotlib ver={matplotlib.__version__}')
    print(f'tf ver={tf.__version__}')
    print(f'tfds ver={tfds.__version__}')    

    unittest.main(exit=False)