#!/usr/bin/env python3
import subprocess
import sys
import os

global totalDirCount 
global totalFileCount 

def tree(path,level):
    content=os.listdir(path)
    count=0
    
    for entry in content:
        if os.path.isfile(path+"/"+entry):
            totalFileCount+=1
            output=""
            for i in range(level-1):
                output=output+"│   "
            if count==len(content)-1:
                output=output+"└── "
            else:
                output=output+"├── "
            print(output+entry)
        else:
            totalDirCount+=1
            tree(path+"/"+entry,level+1)
        count=count+1
        
if __name__ == '__main__':
    # just for demo
    path="."
    totalDirCount=0
    totalFileCount=0

    if len(sys.argv)==2:
        path=sys.argv[1]
    tree(path,0)
    print(totalDirCount," directories, ",totalFileCount," files")
