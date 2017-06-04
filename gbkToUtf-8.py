import os
import codecs
from sys import argv,exit

if len(argv) == 1:
    print u"    useage:gbkToUtf-8 filename targetname"
    exit()

source = argv[1]
if len(argv) == 2:
    target = source
elif len(argv) == 3:
    target = argv[2]

content = codecs.open(source, 'r', 'gbk').read().encode('utf-8')
os.remove(source)

targetFile = open(target, 'w')
targetFile.write(content)
