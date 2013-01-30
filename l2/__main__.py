#!/usr/bin/env python3
import __init__
import os.path
import sys

def getExecPath():
    try:
        sFile = os.path.abspath(sys.modules['__main__'].__file__)
    except:
        sFile = sys.executable
    return os.path.dirname(sFile)

if __name__ == "__main__":
  path = getExecPath()
  print(path)
  __init__.run(path)