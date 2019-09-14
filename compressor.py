'''
Copy all of the files in an input dir into zips in an output dir in bundles of
size `chunksize`:

python compressor.py inpdir outdir [chunksize - default 25]
'''
import os
import shutil
import zipfile
import sys

chunksize = 25

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

if len(sys.argv) < 3:
  print('Please provide in and output directories')
  print(__doc__)
  sys.exit(1)
elif len(sys.argv) > 3:
  chunksize = int(sys.argv[3])

inpdir = sys.argv[1]
outdir = sys.argv[2]
if not os.path.exists(outdir):
  os.makedirs(outdir)

f = []
for (_, _, filenames) in os.walk(inpdir):
  f.extend(filenames)
  break

print('inp dir = {}, out dir = {}, num items = {}, chunk size = {}'.format(
  inpdir, outdir, len(f), chunksize))

current_dir = 1
while len(f) > 0:
  chunk = f[:chunksize]
  f = f[chunksize:]
  newpath = str(current_dir)
  if not os.path.exists(newpath):
    os.makedirs(newpath)
  for filename in chunk:
    shutil.copyfile(
      os.path.join(inpdir, filename),
      os.path.join(newpath, filename))
  zpname = newpath + '.zip'
  zf = zipfile.ZipFile(zpname, 'w')
  for filename in chunk:
    zf.write(os.path.join(newpath, filename))
  zf.close()
  shutil.rmtree(newpath)
  shutil.move(zpname, os.path.join(outdir, zpname))
  current_dir += 1
