#!/usr/bin/env python
# Do the same as awk here:
# df -h | awk '{if ($5 > 75) print $6, $5}'
import fileinput
import re
for line in fileinput.input():
    fields = re.split(r"\s+", line.rstrip())
    try:
        if int(fields[4].rstrip("%")) > 75:
            print(fields[5], fields[4])
    except ValueError:
        pass
