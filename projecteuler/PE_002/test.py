import sys, os
import timeit

sys.path.insert(0, os.getcwd() + '/Python')

from PE_002 import PE_002

file = open("README.md","w")

with open('ProjectEuler.md') as f:
   for line in f:
       file.write(line)

file.write('\n<p align="center">\n')
file.write('    ' + '<b>' + str(PE_002()) + '</b>')
file.write("\n</p>")
file.write("\n\n-----\n\n")

file.write("### Python\n\n")
file.write('<p align="center">\n')
file.write("    {} <b>s</b>".format(timeit.timeit("PE_002()",
                                           setup="from __main__ import PE_002")/1000000))
file.write("\n</p>\n\n")

for f in os.listdir('.'):
    if f.endswith("Python.png"):
        file.write('<p align="center">\n')
        file.write("    <img src={}/>\n".format(f))
        file.write("</p>\n\n")
file.write("-----\n")
file.close()
