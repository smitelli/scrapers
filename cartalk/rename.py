import glob
import os
import re


class FoundItException(Exception):
    pass


for filename in glob.iglob('./result/*'):
    print filename
    base, ext = os.path.splitext(os.path.basename(filename))
    try:
        m = re.match('^#(\d{4}) - (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^#(\d{4})_ (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^01 #(\d{4})_ (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^01-01- #(\d{4}) (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^Car Talk #(\d{4}) - (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^Car Talk (\d{4}) (.+)$', base)
        if m:
            shownum = m.group(1)
            title = m.group(2)
            raise FoundItException()

        m = re.match('^Car Talk (.+) Show #(\d{4})', base)
        if m:
            shownum = m.group(2)
            title = m.group(1)
            raise FoundItException()
    except FoundItException:
        newname = './result/Car Talk - ({}) {}.{}'.format(shownum, title, ext)
        os.rename(filename, newname)
