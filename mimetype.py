import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mm = {}
fs = []
n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    mm.update({ext.upper() : mt})
print >> sys.stderr, "mm: "+str(mm)

for i in xrange(q):
    f = raw_input()  # One file name per line.
    r = re.search('\.\w+$',f)
    if r is None:
        print "UNKNOWN"
        continue
    e = r.group(0)[1:]
    if e.upper() in mm:
        print str(mm[e.upper()])
    else:
        print "UNKNOWN"
