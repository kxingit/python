#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def getFileList(dirname):
  return os.listdir(dirname)

def copy_to(filelist, dirname):
    #  os.mkdir(dirname)
  for filename in filelist:
    match = re.search(r'__(\w+)__', filename)
    if match:
      shutil.copy(filename, dirname)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    sourcedir = args[2]
#    del args[0:2]
    filelist = getFileList(sourcedir)
    copy_to(filelist, todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    sourcedir = args[2]
    filelist = getFileList(sourcedir)
    fileliststr = ''
    for filename in filelist:
      fileliststr = fileliststr + filename + ' '
    cmd = 'zip -j ' + tozip + '/test.zip ' + fileliststr
    print "Command I'm going to do:" + cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
      sys.stderr.write(output)
      sys.exit(1)
#    del args[0:2]
#  filelist = getFileList('.')
#  zip_to(filelist, tozip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
