import glob
import os
import re
import subprocess
import sys


for filename in glob.iglob('./input/*'):
    print filename
    base, ext = os.path.splitext(os.path.basename(filename))

    m = re.search('-([a-zA-Z0-9_-]{11})$', base)
    if not m:
        print 'Could not extract code'
        sys.exit(1)

    url = 'https://www.youtube.com/watch?v={0}'.format(m.group(1))

    tries = 1
    while True:
        if tries > 1:
            print 'Try {0}'.format(tries)
            template = '%(uploader_id)s - %(title)s {0}.%(ext)s'.format(tries)
        else:
            template = '%(uploader_id)s - %(title)s.%(ext)s'

        new_name = subprocess.check_output([
            'youtube-dl', '-s', '--get-filename', '-o', template, url])

        newname = './output/{0}'.format(new_name.strip())

        if os.path.isfile(newname):
            tries += 1
            continue

        os.rename(filename, newname)
        break
