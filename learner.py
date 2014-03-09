#!/usr/bin/env python

import pickle
import numpy as np
import neurolab as nl
from PIL import Image
import os
import shutil

NUM_OF_INPUTS = 128
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
def hist(r):
    rr, rb = np.histogram(r, bins=NUM_OF_INPUTS)
    rr = normalize(rr)
    return rr, rb
def normalize(a):
    b = []
    for x in a:
        b.append(float(x - min(a)) / float(max(a)-min(a)))
    return np.array(b) 

inp = []
tar = []

def add_data(n, r):
    I1 = np.asarray(Image.open(n))
    h = np.concatenate((hist(I1[:,:,0])[0], hist(I1[:,:,1])[0], hist(I1[:,:,2])[0]))
    inp.append(h)
    tar.append([r])
def load_data(n):
    I1 = np.asarray(Image.open(n))
    h = np.concatenate((hist(I1[:,:,0])[0], hist(I1[:,:,1])[0], hist(I1[:,:,2])[0]))
    return h



if __name__ == '__main__':
    net = nl.net.newff([[0.0, 1.0]]*(NUM_OF_INPUTS*3), [5,1])

    # Learning

    try:
        net.layers = pickle.load(open('anime.net'))
    except:
        print 'Learning process required.'
        try:
            inp, tar = pickle.load(open('dataset.dat'))
        except:
            print 'Data set generation required.'
            print 'Adding the data'
            print ' - Positives'
            for x in os.listdir('./IN_P'):
                try:
                    add_data('./IN_P/' + x, 1)
                except:
                    print 'Error', x
            print ' - Negatives'
            for x in os.listdir('./IN_N'):
                try:
                    add_data('./IN_N/' + x, 0)
                except:
                    print 'Error', x
            pickle.dump([inp, tar], open('dataset.dat', 'w'))
        print 'Learning'
        #net.trainf = nl.train.train_gdx
        error = net.train(inp, tar, epochs=1000000, goal=0.00001)
        pickle.dump(net.layers, open('anime.net','w'))
        print net.sim([load_data('./IN_P/100.jpg')])
        print net.sim([load_data('./IN_N/101.jpg')])
        print 'Done'


    if raw_input('This program is trying to sort the photos. Y?')=='Y':
        for x in os.listdir('./src'):
            if x.endswith('jpg') or x.endswith('jpeg') or x.endswith('png'):
                try:
                    d = net.sim([load_data('./src/' + x)])[0]
                    if d >= 0.7:
                        shutil.copyfile('./src/' + x, './OUT_P/' + x)
                    elif d <= 0.3:
                        shutil.copyfile('./src/' + x, './OUT_N/' + x)
                    else:
                        shutil.copyfile('./src/' + x, './OUT_X/' + x)
                    print d, x
                except:
                    print 'Error', x
