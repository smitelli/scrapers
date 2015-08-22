import sqlite3
import sys
import urllib2

create = """
CREATE TABLE codepoints(
    cid INT PRIMARY KEY NOT NULL,
    svg TEXT
);
"""

conn = sqlite3.connect('codepoints.sqlite')
c = conn.cursor()
c.execute(create)
for cid in xrange(0x10ffff, 0x110000):
    hid = hex(cid)[2:]
    url = 'http://www.fileformat.info/info/unicode/char/{}/svg.svg'.format(hid)
    svg = None
    print '0x{}...'.format(hid)
    for _ in xrange(10):
        try:
            req = urllib2.urlopen(url)
            charset = req.headers['content-type'].split('charset=')[-1]
            svg = unicode(req.read(), charset)
            if svg:
                break
            print "HMM..."
        except Exception:
            print "UH-OH..."
            pass
    if not svg:
        print "Something is wrong!"
        sys.exit(1)
    c.execute('INSERT INTO codepoints (cid, svg) VALUES (?, ?)', (cid, svg))
    if cid % 10 == 0:
        print "c"
        conn.commit()
conn.commit()
conn.close()
