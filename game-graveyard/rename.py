import glob
import os
import urllib


for filename in glob.iglob('./result/*'):
    base, ext = os.path.splitext(os.path.basename(filename))

    newname = './result/{}{}'.format(urllib.unquote(base), ext)

    if newname == filename:
        continue

    print '{} -> {}'.format(filename, newname)
    os.rename(filename, newname)
