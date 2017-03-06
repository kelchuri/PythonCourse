__author__ = 'Kalyan'

notes = '''
Continuing on our theme of actually measuring how long our programs take, I would like you use the code below to
understand profiling in python.

Using time.clock() will be sufficient if you are looking at method level granularity. But if you are looking to dig deeper
using it before and after every suspect line is tedious. For such scenarios profilers are very useful to give you a clear
idea of where your program is spending time.

Read up on the cProfile module at http://docs.python.org/2/library/profile.html and use it on this on the
create_file_numbers_old and figure out the main bottleneck. Rewrite create_file_numbers_new to address this bottleneck
to get at least 5-10 times speed up.
'''
import cStringIO
import functools
import inspect
import os
import sys
import time
import cProfile
import re
import argparse
from collections import Counter


def create_file_numbers_old(filename, size):
    start = time.clock()

    value = 0
    with open(filename, "w") as f:
        while f.tell()< size:
            f.write("{0}\n".format(value))
            value += 1

    end = time.clock()
    print "time taken to write a file of size OLD", size, " is ", (end -start), "seconds \n"

def create_file_numbers_new(filename, size):
    time1= time.clock()
   # f=cStringIO.StringIO()
    f=open(filename,"wb")
    value=0
    leng=0
    while leng<size:
         f.write("%s\n"%value)
         leng=leng+(len(str(value))+1)
         value+=1

    time2= time.clock()
    f.close()
    print "time taken to write a file of size NEW",size,"is",time2-time1

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    return os.path.dirname(mod_file)

output_path = functools.partial(os.path.join, get_module_dir())

#pass file name and size from command line
def main(argv = sys.argv):
    #add argument checking and parsing here ..
    parser= argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--size",type=int)
    args=parser.parse_args()
    fpath = output_path("test.txt")
    create_file_numbers_old(fpath, 50*1024*1024) #write a 50M file
    cProfile.run('re.compile("create_file_numbers_old(fpath,25*1024*1024)")')
    fpath1= output_path(args.name)
    create_file_numbers_new(fpath1,args.size)
    cProfile.run('re.compile("create_file_numbers_new(fpath1,args.size)")')
if __name__ == "__main__":
    main()


my_analysis = '''
A useless looping structure eats the execution time up,eg in the old func
with the file open as will be executed every time the loop is true and also formatting
Most importantly.. f.tell() takes away alot of time
'''
