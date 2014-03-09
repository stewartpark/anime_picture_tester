import shutil
import os

i = 0
for x in os.listdir('./IN_P'):
    i = i + 1
    os.rename('./IN_P/' + x, './IN_P/' + str(i) + '.' + x.split('.')[-1])
i = 0
for x in os.listdir('./IN_N'):
    i = i + 1
    os.rename('./IN_N/' + x, './IN_N/' + str(i) + '.' + x.split('.')[-1])

os.system('rm -f OUT_?/*')
