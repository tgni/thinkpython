#os.path.walk(path, visit, arg)
def visit(arg, dir, names):
    print dir, names

import os
cwd = os.getcwd()
arg = 1
os.path.walk(cwd, visit, arg)
