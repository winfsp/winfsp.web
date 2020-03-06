#!/usr/bin/python

import re, sys

order = []
assoc = {}

for line in sys.stdin:
    line = line.rstrip()
    rslt = re.search("(\$[A-Za-z0-9_-]+):[ \t]*(#[0-9A-Fa-f]+[^;]*;)", line)
    if not rslt:
        rslt = re.search("(\$[A-Za-z0-9_-]+):[ \t]*(rgba[^;]*;)", line)
    if rslt:
        order.append(rslt)
        assoc[rslt.group(1)] = rslt.group(2)
    else:
        order.append(line)

for i in range(len(order)):
    if hasattr(order[i], "group"):
        name = order[i].group(1)
        if "$white" == name:
            order[i] = "%s: %s" % (name, assoc["$black"])
        elif "$black" == name:
            order[i] = "%s: %s" % (name, assoc["$white"])
        elif re.search(".*-fade-[0-9]+", name):
            rslt = re.search("(.*-fade-)([0-9]+)", name)
            valu = int(rslt.group(2))
            valu = 100 - valu
            order[i] = "%s: %s" % (name, assoc["%s%02d" % (rslt.group(1), valu)])
        elif re.search(".*-[0-9]+", name):
            rslt = re.search("(.*-)([0-9]+)", name)
            valu = int(rslt.group(2))
            valu = 900 - valu
            order[i] = "%s: %s" % (name, assoc["%s%03d" % (rslt.group(1), valu)])

for line in order:
    print(line)
