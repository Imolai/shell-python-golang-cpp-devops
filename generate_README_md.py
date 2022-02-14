#!/usr/bin/env python
import os
import re
import sys
import subprocess

input = 'README.src.md'
output = 'README.md'
try:
    ifh = open(input, 'r')
    ofh = open(output, 'w')
except OSError as err:
    print(err, file=sys.stderr)
    exit(1)

print(f"Generating '{output}' from '{input}' and sources in 'src/'.")
for line in ifh:
    line_import = re.match(r'^\[\[(.*)\]\]$', line)
    if line_import:
        if os.path.exists(line_import[1]):
            with open(line_import[1]) as src:
                ofh.write(src.read())
        else:
            print(line, file=sys.stderr)
            exit(1)
    else:
        ofh.write(line)
ifh.close()
ofh.close()

try:
    retcode = subprocess.call('doctoc --title "## contents"' + output, shell=True)
    if retcode < 0:
        print("Doctoc was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Doctoc returned", retcode, file=sys.stderr)
except OSError as err:
    print("Execution failed:", err, file=sys.stderr)
