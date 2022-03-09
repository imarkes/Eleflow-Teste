import glob
import os

path = 'AIR_CIA'
csv_files = glob.glob(os.path.join(path, '*.csv'))
print(csv_files)
#print(os.listdir(path))

#filename = f' {path}/'.join(os.listdir(path)).split()
#print(filename)