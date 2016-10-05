#!/usr/bin/env python3
import subprocess
import sys
import os

global totalDirCount
global totalFileCount

def display(path):
    print(".")
    tree(path,0)
    print(totalDirCount," directories, ",totalFileCount," files")

def tree(path,level):
    content=sorted(os.listdir(path))
    count=0
    for entry in content:
        indent=""
        for i in range(level-1):
            indent=indent+"│   "
        if count==len(content)-1:
            indent=indent+"└── "
        else:
            indent=indent+"├── "
        if os.path.isfile(path+"/"+entry):
            print(indent+entry)
            totalDirCount+=1
        else:            
            print(indent+entry)
            totalFileCount+=1
            tree(path+"/"+entry,level+1)
        count=count+1
        
if __name__ == '__main__':
    # just for demo
    path="."
    totalDirCount=0
    totalFileCount=0
    if len(sys.argv)==2:
        path=sys.argv[1]
    display(path)
    
