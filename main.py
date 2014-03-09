#!/usr/bin/env python

import learner
import pickle 
import neurolab as nl

net = nl.net.newff([[0.0, 1.0]]*(learner.NUM_OF_INPUTS*3), [5,1])
net.layers = pickle.load(open('./anime.net'))
p = raw_input('File path:')
o = net.sim([learner.load_data(p)])[0]
print o
if o >= 0.6:
    print 'Anime picture'
elif o <= 0.4:
    print 'Real picture'
else:
    print 'Can\'t decide'

